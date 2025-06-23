# app/auth/deps.py

from fastapi import Request, HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
import os
import requests
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.deps import get_db
from app.models import User
from app.services.user_service import get_user_by_auth0

# Load .env variables
load_dotenv()

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE")
ALGORITHMS = os.getenv("ALGORITHMS", "RS256")

http_bearer = HTTPBearer()

# ✅ Verifies JWT token using Auth0's JWKS endpoint
async def verify_jwt(
    credentials: HTTPAuthorizationCredentials = Security(http_bearer)
):
    token = credentials.credentials
    try:
        header = jwt.get_unverified_header(token)
        jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
        jwks = requests.get(jwks_url).json()

        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }

        if rsa_key:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=[ALGORITHMS],
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
            return payload
        else:
            raise HTTPException(status_code=401, detail="Unable to verify token")

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ✅ Dependency to extract current user from Auth0 token & load/create DB user
async def get_current_user(
    payload: dict = Depends(verify_jwt), db: AsyncSession = Depends(get_db)
):
    auth0_id = payload.get("sub")
    email = payload.get("email", "unknown@example.com")

    user = await get_user_by_auth0(db, auth0_id)
    if not user:
        # Auto-register the user if not found
        user = User(auth0_id=auth0_id, email=email)
        db.add(user)
        await db.commit()
        await db.refresh(user)

    return {"id": user.id, "sub": user.auth0_id}
