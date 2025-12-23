import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("❌ OPENAI_API_KEY not found. Check .env file")

SYSTEM_PROMPT = """
You are an expert rule engine assistant.
Convert user text into STRICT JSON for Durable Rules.

Return ONLY valid JSON in this format:
{
  "ruleset": "policy",
  "conditions": [
    {"field": "vehicle_age", "operator": ">", "value": 10}
  ],
  "action": {
    "decision": "reject"
  }
}
"""

def text_to_rule_json(user_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0
    )

    return response.choices[0].message.content
