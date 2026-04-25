from openai import OpenAI
from django.conf import settings

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url='https://api.groq.com/openai/v1'
)


def generate_post(thought, tone, audience):
    prompt = f"""
    You are a professional LinkedIn content writer.

    Convert the following idea into a HIGH-QUALITY LinkedIn post.

    Thought: {thought}
    Tone: {tone}
    Audience: {audience}

    IMPORTANT RULES:
    - Make it look like a REAL viral LinkedIn post
    - Use spacing (short paragraphs)
    - Add emojis naturally (not too many)
    - Make hook powerful (1 line)
    - Main content should have bullet points OR short lines OR use relavent emoji 
    - Add storytelling feel if possible
    - End with strong CTA
    - Add 5 relevant hashtags at the end

    FORMAT EXACTLY LIKE THIS:

    🔥 Hook (1 line)

    Main Content:
    👉 Point 1
    👉 Point 2
    👉 Point 3

    CTA (1–2 lines)

    #hashtag1 #hashtag2 #hashtag3 #hashtag4 #hashtag5
    """

    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[{'role': 'user', 'content': prompt}]
    )

    return response.choices[0].message.content

# 📅 Best posting time helper
# def get_best_posting_time(country):
#     timing = {
#         "Bangladesh": "Tue–Thu, 9:00 AM BST",
#         "USA": "Tue–Thu, 8:00 AM EST",
#         "UK": "Tue–Thu, 9:00 AM GMT",
#         "India": "Tue–Thu, 8:30 AM IST",
#         "UAE": "Tue–Thu, 9:00 AM GST",
#     }

#     return timing.get(country, "Tue–Thu, 9:00 AM")