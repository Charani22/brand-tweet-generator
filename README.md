# BrandVoice AI — On-brand Tweet Generator

A small Streamlit application that takes brand and campaign details, infers a plausible brand voice using an LLM, and generates 10 varied tweet drafts.

## Features

- Brand name, industry, campaign objective, products/services, preferred tone, and audience inputs
- Prompt-based brand voice inference
- Exactly 10 tweet drafts in a mixture of styles
- Brand voice summary with 3–4 bullets
- JSON download for generated results
- API key entered at runtime or provided through an environment variable

## Technology

- Python
- Streamlit
- OpenAI API (`gpt-4o-mini`)
- Prompt engineering with structured JSON output

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

6. Open the local address printed in the terminal, usually `http://localhost:8501`.
7. Enter an OpenAI API key in the sidebar and fill in the form.

You can also set the key in your terminal before starting the app.

**Windows PowerShell**
```powershell
$env:OPENAI_API_KEY="your-api-key"
streamlit run app.py
```

**macOS/Linux**
```bash
export OPENAI_API_KEY="your-api-key"
streamlit run app.py
```

Do not commit API keys to GitHub or put them directly into source code. API use may incur charges.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload `app.py`, `requirements.txt`, `README.md`, `APPROACH.md`, and `SAMPLE_OUTPUTS.md`.
2. Open Streamlit Community Cloud: https://share.streamlit.io/
3. Connect your GitHub account and select the repository and `app.py`.
4. In the app's deployment settings, add a secret named `OPENAI_API_KEY`.
5. Deploy and test the public URL in a private/incognito browser window.

Example secret format:
```toml
OPENAI_API_KEY = "your-api-key"
```

Never commit the secrets file to your repository.

## How to test

Try at least two brands with contrasting inputs. For example:
- Nike — Sportswear; engagement; running shoes and sportswear; bold and motivational
- Starbucks — Coffee; brand awareness; coffee and café experience; warm and friendly

The examples are test scenarios. The application does not scrape current posts or claim that generated copy was published by the brand.

## Limitations and responsible use

- Brand voice is inferred from user inputs and any examples the user provides. It is not verified against live social media accounts.
- Generated posts may be inaccurate or unsuitable; review them before publishing.
- Do not enter confidential campaign details or personal data.
- This prototype uses the OpenAI API, so internet access and a valid API key are required.
