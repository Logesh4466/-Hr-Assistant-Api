from openai import AzureOpenAI
from .config import settings
from typing import List, Tuple
import logging

# Simple wrapper for Azure OpenAI chat usage
class AIClient:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
            api_key=settings.AZURE_OPENAI_API_KEY,
            api_version=settings.AZURE_OPENAI_API_VERSION
        )
        self.deployment = settings.AZURE_OPENAI_DEPLOYMENT_NAME

    def guess_best_template(self, user_query: str, templates: List[str]) -> str:
        prompt = f"""
User wants: "{user_query}"
Templates available: {templates}

Return ONLY the best matching file name (one filename exactly as it appears in the list).
"""
        resp = self.client.chat.completions.create(
            model=self.deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        # strip and return
        result = resp.choices[0].message.content.strip()
        return result

    def build_questions_for_placeholders(self, placeholders: List[str]) -> List[Tuple[str, str]]:
        if not placeholders:
            return []

        prompt = f"""
The document contains these fillable placeholders:
{placeholders}

For each placeholder, generate:
- A clear, short question to ask the user (in German or English depending on placeholder language).
- Do NOT translate placeholders.

Return output as lines in the form:
placeholder:::question
"""
        resp = self.client.chat.completions.create(
            model=self.deployment,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        text = resp.choices[0].message.content.strip()
        pairs = []
        for line in text.splitlines():
            if ":::" in line:
                p, q = line.split(":::", 1)
                pairs.append((p.strip(), q.strip()))
        return pairs
