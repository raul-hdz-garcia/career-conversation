import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

from styles import create_ui
from tools import TOOLS, handle_tool_calls

load_dotenv(override=True)



PROFILE_DIR = Path(__file__).resolve().parent


class Me:
    def __init__(self):
        self.openai = OpenAI()
        self.name = "Raul Hernandez"
        self.linkedin = ""
        reader = PdfReader(PROFILE_DIR / "linkedin.pdf")
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        with open(PROFILE_DIR / "summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def system_prompt(self):
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
However, if the question is not related to career, background, skills or experience, you should lead the conversation back to the topic of career, background, skills or experience. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        system_prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return system_prompt

    def chat(self, message, history):
        messages = [
            {"role": "system", "content": self.system_prompt()}
        ] + history + [{"role": "user", "content": message}]
        done = False
        while not done:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini", messages=messages, tools=TOOLS
            )
            if response.choices[0].finish_reason == "tool_calls":
                message = response.choices[0].message
                results = handle_tool_calls(message.tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        return response.choices[0].message.content


if __name__ == "__main__":
    me = Me()
    demo = create_ui(me.chat, me.name)
    port = int(os.getenv("PORT", "7860"))
    demo.launch(server_name="0.0.0.0", server_port=port, ssr_mode=False)
