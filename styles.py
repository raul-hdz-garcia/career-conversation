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
    padding-top: 1.5rem !important;
    font-family: "DM Sans", sans-serif;
}

.hero {
    background: linear-gradient(135deg, #12203a 0%, #0f3d3a 100%);
    border: 1px solid #2a3a57;
    border-radius: 20px;
    padding: 28px 32px 22px;
    margin-bottom: 16px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28);
}

.hero h1 {
    color: #f8fafc;
    font-size: 2rem;
    font-weight: 700;
    margin: 0 0 8px 0;
    letter-spacing: -0.03em;
}

.hero p {
    color: #b7c7db;
    font-size: 1.02rem;
    line-height: 1.5;
    margin: 0;
}

.badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 16px;
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
    min-height: 460px;
}

footer.site-footer {
    color: #7f93ad;
    font-size: 0.85rem;
    text-align: center;
    margin-top: 8px;
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
                height=480,
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
