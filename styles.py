import gradio as gr

THEME = gr.themes.Base(
    primary_hue="indigo",
    secondary_hue="violet",
    neutral_hue="gray",
    font=gr.themes.GoogleFont("Plus Jakarta Sans"),
    font_mono=gr.themes.GoogleFont("JetBrains Mono"),
).set(
    body_background_fill="#f5f6fa",
    body_text_color="#1f2430",
    block_background_fill="#ffffff",
    block_border_color="#e4e6ef",
    block_label_background_fill="#ffffff",
    block_label_text_color="#6b7280",
    block_radius="16px",
    background_fill_secondary="#eef0f8",
    button_primary_background_fill="#4f46e5",
    button_primary_background_fill_hover="#4338ca",
    button_primary_text_color="#ffffff",
    button_secondary_background_fill="#ffffff",
    button_secondary_border_color="#dcdfec",
    button_secondary_text_color="#3f455a",
    input_background_fill="#ffffff",
    input_border_color="#dcdfec",
    input_radius="12px",
)

CSS = """
.gradio-container {
    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 1.25rem 1rem 0.5rem !important;
}

.topbar {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #ffffff;
    border: 1px solid #e4e6ef;
    border-radius: 18px;
    padding: 16px 20px;
    margin-bottom: 14px;
}

.avatar {
    width: 48px;
    height: 48px;
    flex: 0 0 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4f46e5 0%, #a855f7 100%);
    color: #ffffff;
    font-weight: 700;
    font-size: 1.05rem;
    letter-spacing: 0.04em;
    display: flex;
    align-items: center;
    justify-content: center;
}

.topbar-text h1 {
    margin: 0;
    font-size: 1.2rem;
    font-weight: 700;
    color: #171a23;
}

.topbar-text p {
    margin: 2px 0 0;
    font-size: 0.88rem;
    color: #6b7280;
}

.status {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 7px;
    font-size: 0.8rem;
    font-weight: 600;
    color: #047857;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
    border-radius: 999px;
    padding: 6px 12px;
}

.status span {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #10b981;
}

.card {
    background: #ffffff;
    border: 1px solid #e4e6ef;
    border-radius: 16px;
    padding: 16px 18px;
    margin-bottom: 12px;
}

.card h2 {
    margin: 0 0 10px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: #8b90a3;
}

.card ul {
    margin: 0;
    padding: 0;
    list-style: none;
}

.card li {
    font-size: 0.88rem;
    color: #3f455a;
    padding: 5px 0;
    border-bottom: 1px dashed #edeef5;
}

.card li:last-child {
    border-bottom: none;
}

.card li b {
    color: #171a23;
    font-weight: 600;
}

.side-label {
    margin: 4px 0 8px 4px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.09em;
    color: #8b90a3;
}

.tip {
    font-size: 0.85rem;
    line-height: 1.5;
    color: #4b5163;
    margin: 0;
}

#side-buttons button {
    width: 100%;
    text-align: left !important;
    justify-content: flex-start !important;
    font-size: 0.86rem !important;
    font-weight: 500 !important;
    padding: 9px 12px !important;
    margin-bottom: 6px !important;
    border-radius: 10px !important;
}

#side-buttons button:hover {
    background: #eef0fe !important;
    border-color: #c7cbfa !important;
    color: #4338ca !important;
}

#chat-panel {
    background: #ffffff;
    border: 1px solid #e4e6ef;
    border-radius: 18px;
    padding: 10px 12px 4px;
}

#chatbot {
    border: none !important;
    background: transparent !important;
}

/* Gradio nests three elements per message, each of which draws its own box.
   Strip them all, then paint only the outer bubble so the text sits on a
   single flat fill with no inner outlines. */
#chatbot .message,
#chatbot .message-row .message,
#chatbot [data-testid="bot"],
#chatbot [data-testid="user"],
#chatbot .message-content {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 0.93rem !important;
    line-height: 1.55 !important;
}

#chatbot .bot.message {
    background: #f4f5fb !important;
    color: #23283a !important;
    border-radius: 14px 14px 14px 4px !important;
    box-shadow: 0 1px 1px rgba(16, 20, 40, 0.07) !important;
}

#chatbot .user.message {
    background: #4f46e5 !important;
    color: #ffffff !important;
    border-radius: 14px 14px 4px 14px !important;
    box-shadow: 0 1px 1px rgba(16, 20, 40, 0.07) !important;
}

#chatbot [data-testid="bot"] *,
#chatbot [data-testid="user"] * {
    color: inherit !important;
}

/* Keep the composer at its natural height as the transcript grows. */
#msg-box,
#chat-panel .gr-group,
#chat-panel .styler {
    flex: 0 0 auto !important;
}

.foot {
    text-align: center;
    font-size: 0.78rem;
    color: #9096a8;
    padding: 10px 0 4px;
}
"""


def _initials(name: str) -> str:
    parts = [p for p in name.split() if p]
    return "".join(p[0].upper() for p in parts[:2]) or "AI"


def _topbar_html(name: str) -> str:
    return f"""
    <div class="topbar">
        <div class="avatar">{_initials(name)}</div>
        <div class="topbar-text">
            <h1>{name}</h1>
            <p>Software engineer · digital twin</p>
        </div>
        <div class="status"><span></span>Open to conversations</div>
    </div>
    """


PROFILE_HTML = """
<div class="card">
    <h2>Profile</h2>
    <ul>
        <li><b>Role</b> — Software engineer</li>
        <li><b>Based in</b> — Guadalajara, Mexico</li>
        <li><b>Learning</b> — Chinese &amp; cooking</li>
        <li><b>Off the clock</b> — Travel and nature</li>
    </ul>
</div>
"""

CONTACT_HTML = """
<div class="card">
    <h2>Get in touch</h2>
    <p class="tip">Share your email in the chat and it gets passed along
    directly — no forms, no waiting.</p>
</div>
"""

# Gradio disables the textarea while a reply is in flight, which blurs it, and
# re-enables it without restoring focus. Watching that attribute is what keeps
# the caret in the composer; Gradio's own change event never reaches the DOM
# here. The guard keeps focus from being yanked away from anywhere else the
# user is working.
FOCUS_COMPOSER_JS = """
() => {
    const composer = () => document.querySelector('#msg-box textarea');

    const idle = () => {
        const active = document.activeElement;
        return !active
            || active === document.body
            || active.closest('#msg-box')
            || active.closest('#side-buttons');
    };

    const grab = () => {
        const box = composer();
        if (!box || box.disabled || !idle()) return;
        box.focus({ preventScroll: true });
        box.selectionStart = box.selectionEnd = box.value.length;
    };

    const grabSoon = () => [0, 80, 250].forEach(d => setTimeout(grab, d));

    // A multi-line draft leaves an inline height on the textarea and the page
    // scrolled down to it. Gradio clears the text but not either of those, so
    // undo them once the send has actually gone through.
    const reset = () => {
        let tries = 0;
        const tick = setInterval(() => {
            const box = composer();
            if (box && box.value === '') {
                box.style.height = '';
                box.style.overflowY = '';
                window.scrollTo({ top: 0, behavior: 'smooth' });
                clearInterval(tick);
            }
            if (++tries > 40) clearInterval(tick);
        }, 50);
    };

    document.addEventListener('click', (e) => {
        if (e.target.closest('#msg-box button')) {
            grabSoon();
            reset();
        } else if (e.target.closest('#side-buttons button')) {
            grabSoon();
        }
    }, true);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey && e.target.closest('#msg-box')) {
            grabSoon();
            reset();
        }
    }, true);

    const watch = () => {
        const shell = document.querySelector('#msg-box');
        if (!shell) return setTimeout(watch, 300);
        new MutationObserver(grabSoon).observe(shell, {
            attributes: true,
            attributeFilter: ['disabled'],
            subtree: true,
        });
    };
    watch();
}
"""

PROMPTS = [
    "Walk me through your background",
    "What technologies do you work with?",
    "What are you learning right now?",
    "What kind of role are you looking for?",
    "How can I contact you?",
]


def create_ui(chat_fn, name: str):
    with gr.Blocks(
        theme=THEME, css=CSS, js=FOCUS_COMPOSER_JS, title=f"{name} — Digital Twin"
    ) as demo:
        gr.HTML(_topbar_html(name))

        with gr.Row(equal_height=False):
            with gr.Column(scale=3, min_width=240):
                gr.HTML(PROFILE_HTML)
                with gr.Column(elem_id="side-buttons"):
                    gr.HTML('<p class="side-label">Start with</p>')
                    prompt_buttons = [
                        gr.Button(text, size="sm", variant="secondary")
                        for text in PROMPTS
                    ]
                gr.HTML(CONTACT_HTML)

            with gr.Column(scale=7, min_width=420, elem_id="chat-panel"):
                chat = gr.ChatInterface(
                    chat_fn,
                    type="messages",
                    chatbot=gr.Chatbot(
                        elem_id="chatbot",
                        type="messages",
                        height=440,
                        show_label=False,
                        value=[
                            {
                                "role": "assistant",
                                "content": (
                                    f"Hi, I'm {name}'s digital twin. Ask me about "
                                    "experience, skills, or projects — or leave an "
                                    "email and I'll make sure it reaches him."
                                ),
                            }
                        ],
                    ),
                    textbox=gr.Textbox(
                        elem_id="msg-box",
                        placeholder=f"Message {name.split()[0]}…",
                        container=False,
                        scale=7,
                        submit_btn=True,
                        stop_btn=True,
                    ),
                )

        for button in prompt_buttons:
            button.click(lambda text=button.value: text, outputs=chat.textbox)

        gr.HTML(f'<div class="foot">Digital twin of {name} · GPT-4o mini</div>')

    return demo
