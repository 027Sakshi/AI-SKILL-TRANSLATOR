from pydantic import BaseModel, Field
from typing import Optional


class UserProfile(BaseModel):
    education: Optional[str] = Field(
        None, description="Highest education qualification"
    )
    experience: Optional[str] = Field(
        None, description="Work experience or internships"
    )
    skills_text: str = Field(
        ..., description="Raw text describing skills"
    )
