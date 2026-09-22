import gradio as gr

THEME = gr.themes.Soft(
    primary_hue="teal",
    secondary_hue="slate",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("DM Sans"),
    font_mono=gr.themes.GoogleFont("IBM Plex Mono"),
).set(
    body_background_fill="#0b1220",
    body_background_fill_dark="#0b1220",
    body_text_color="#e8eef7",
    body_text_color_dark="#e8eef7",
    block_background_fill="#121a2b",
    block_background_fill_dark="#121a2b",
    block_border_color="#243049",
    block_border_color_dark="#243049",
    block_label_text_color="#9db0c9",
    block_title_text_color="#f4f7fb",
    background_fill_secondary="#1b2942",
    background_fill_secondary_dark="#1b2942",
    color_accent_soft="#0f766e",
    color_accent_soft_dark="#0f766e",
    button_primary_background_fill="#14b8a6",
    button_primary_background_fill_hover="#2dd4bf",
    button_primary_text_color="#042f2e",
    input_background_fill="#0f1726",
    input_border_color="#2a3a57",
)

CSS = """
.gradio-container {
    max-width: 920px !important;
    margin: 0 auto !important;
    padding-top: 0.75rem !important;
    font-family: "DM Sans", sans-serif;
}

.hero {
    background: linear-gradient(135deg, #12203a 0%, #0f3d3a 100%);
    border: 1px solid #2a3a57;
    border-radius: 16px;
    padding: 16px 24px 14px;
    margin-bottom: 10px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28);
}

.hero h1 {
    color: #f8fafc;
    font-size: 1.5rem;
    font-weight: 700;
    margin: 0 0 4px 0;
    letter-spacing: -0.03em;
}

.hero p {
    color: #c6d4e6;
    font-size: 0.95rem;
    line-height: 1.4;
    margin: 0;
}

.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 10px;
}

.badge {
    background: rgba(20, 184, 166, 0.14);
    color: #5eead4;
    border: 1px solid rgba(45, 212, 191, 0.35);
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}

#chatbot {
    border: 1px solid #2a3a57 !important;
    height: calc(100vh - 330px) !important;
    min-height: 220px !important;
    max-height: 520px !important;
}

#chatbot .message,
#chatbot .message-row .message {
    border-radius: 14px !important;
    line-height: 1.55;
}

#chatbot .message.bot,
#chatbot .bot .message,
#chatbot [data-testid="bot"] {
    background: #1b2942 !important;
    border: 1px solid #33456a !important;
    color: #eef4fc !important;
}

#chatbot .message.user,
#chatbot .user .message,
#chatbot [data-testid="user"] {
    background: #0f766e !important;
    border: 1px solid #2dd4bf !important;
    color: #f0fdfa !important;
}

#chatbot .message p,
#chatbot .message li,
#chatbot .message span,
#chatbot [data-testid="bot"] *,
#chatbot [data-testid="user"] * {
    color: inherit !important;
}

#chatbot .message a {
    color: #7dd3fc !important;
    text-decoration: underline;
}

footer.site-footer {
    color: #93a7c0;
    font-size: 0.82rem;
    text-align: center;
    margin-top: 6px;
}
"""


def _hero_html(name: str) -> str:
    return f"""
    <div class="hero">
        <h1>{name}</h1>
        <p>Ask about background, skills, and experience — or leave your email to get in touch.</p>
        <div class="badge-row">
            <span class="badge">Software engineer</span>
            <span class="badge">Guadalajara</span>
            <span class="badge">Career twin</span>
        </div>
    </div>
    """


def create_ui(chat_fn, name: str):
    examples = [
        "What is your background?",
        "What are you learning right now?",
        "I'd like to get in touch — how should I reach you?",
    ]

    with gr.Blocks(theme=THEME, css=CSS, title=f"{name} · Career Twin") as demo:
        gr.HTML(_hero_html(name))
        gr.ChatInterface(
            chat_fn,
            type="messages",
            chatbot=gr.Chatbot(
                elem_id="chatbot",
                label=f"Chat with {name}",
                type="messages",
                height=360,
                avatar_images=(None, None),
            ),
            textbox=gr.Textbox(
                placeholder="Ask about career, projects, or how to get in touch…",
                container=False,
                scale=7,
            ),
            examples=examples,
            cache_examples=False,
        )
        gr.HTML(
            f'<footer class="site-footer">Digital twin of {name} · powered by GPT-4o mini</footer>'
        )

    return demo
