import streamlit as st
import random

st.set_page_config(
    page_title="AI Tweet Generator",
    page_icon="🐦",
    layout="wide"
)

st.title("🐦 AI Brand Tweet Generator")
st.write("Generate 10 brand-focused tweets without an API key!")

# Input form
brand = st.text_input("Brand name", placeholder="e.g. Nike")

industry = st.text_input(
    "Industry / category (optional)",
    placeholder="e.g. sportswear"
)

products = st.text_input(
    "Products or services",
    placeholder="e.g. running shoes, sportswear"
)

tone = st.selectbox(
    "Preferred tone",
    [
        "Bold and motivational",
        "Professional",
        "Friendly",
        "Funny",
        "Inspirational"
    ]
)

audience = st.text_input(
    "Target audience (optional)",
    placeholder="e.g. athletes and fitness enthusiasts"
)

objective = st.selectbox(
    "Campaign objective",
    [
        "Engagement",
        "Brand Awareness",
        "Product Promotion",
        "Website Traffic",
        "Community Building"
    ]
)

context = st.text_area(
    "Extra brand context (optional)",
    placeholder="Describe your brand, campaign, or message."
)


def generate_tweets(brand, industry, products,
                    tone, audience, objective, context):

    brand = brand.strip()
    products = products.strip() or "our latest products"
    industry = industry.strip() or "our community"
    audience = audience.strip() or "everyone"
    context = context.strip()

    hashtags = [
        "#Motivation",
        "#Innovation",
        "#StayInspired",
        "#YourGoals",
        "#Community",
        "#ExploreMore",
        "#MakeItHappen",
        "#NewPossibilities",
        "#KeepGrowing",
        "#TakeTheNextStep"
    ]

    templates = [
        "Ready to take things to the next level? 🚀 Discover {products} with {brand}. {context}",

        "Big goals start with small steps. 💪 Keep moving forward with {brand}! {context}",

        "Your next favorite could be waiting for you. 👀 Explore {products} from {brand}.",

        "Progress over perfection. Every single day. 🔥 That's the spirit of {brand}!",

        "Hey, {audience}! 👋 What's one goal you're working towards today?",

        "Good things happen when passion meets action. ✨ Let's make it happen with {brand}!",

        "It's not just about where you start. It's about how far you go. 💯 #KeepGrowing",

        "Let's talk about {products}! What matters most to you when choosing the right product?",

        "New ideas. Fresh energy. Endless possibilities. 🌟 That's what we're bringing to {industry}.",

        "Your goals deserve your best effort. 💥 Take the next step with {brand} today!"
    ]

    if tone == "Funny":
        templates = [
            "My motivation said 'five more minutes.' My goals said 'let's go!' 😂 Team {brand}!",
            "Warning: Exploring {products} may cause serious excitement! 😎",
            "Dear goals, we're coming for you. No excuses today! 💪 #MakeItHappen",
            "Coffee? Check. Motivation? Check. Ready to go? Absolutely! 🚀",
            "Hey, {audience}! What's your superpower? Ours is bringing fresh ideas!",
            "Some days you win, some days you learn. Either way, keep going! 😄",
            "Your future self is cheering for you already. Don't let them down! 🔥",
            "Quick question: Are you scrolling or making moves today? 👀",
            "Life is too short for boring goals. Dream big with {brand}!",
            "Tag someone who needs a little motivation today! 🙌"
        ]

    elif tone == "Professional":
        templates = [
            "{brand} is committed to helping customers discover better possibilities.",
            "Discover how {products} can support your goals with {brand}.",
            "Innovation begins with understanding what matters to our customers.",
            "At {brand}, we believe meaningful progress starts with clear goals.",
            "We value the trust of our community. Thank you for growing with us.",
            "Explore new possibilities with {brand} and take your next step forward.",
            "Our focus remains on delivering value to {audience}.",
            "What does innovation mean to you? Share your thoughts with us.",
            "Building better experiences starts with listening to our community.",
            "Join {brand} as we continue working towards new possibilities."
        ]

    # Personalize all tweets using the form inputs.
    tweets = []

    for template in templates:
        tweet = template.format(
            brand=brand,
            products=products,
            industry=industry,
            audience=audience,
            context=context
        )

        if context and "{context}" not in template:
            pass

        tweets.append(tweet)

    # Add hashtags and remove accidental empty spaces.
    results = []

    for i, tweet in enumerate(tweets):
        hashtag = hashtags[i]

        if hashtag not in tweet:
            tweet = tweet.strip() + " " + hashtag

        results.append(tweet.strip())

    # Objective-specific final message.
    if objective == "Engagement":
        results[4] += " Share your thoughts below!"
    elif objective == "Brand Awareness":
        results[0] += " Follow us for more!"
    elif objective == "Product Promotion":
        results[2] += " Discover more today!"
    elif objective == "Website Traffic":
        results[8] += " Visit our website to learn more."
    elif objective == "Community Building":
        results[4] += " Let's build something great together!"

    return results


if st.button("Generate 10 tweets", type="primary"):

    if not brand.strip():
        st.error("Please enter a brand name.")
    else:
        tweets = generate_tweets(
            brand,
            industry,
            products,
            tone,
            audience,
            objective,
            context
        )

        st.success("10 tweets generated successfully!")

        for i, tweet in enumerate(tweets, start=1):
            st.markdown(f"### Tweet {i}")
            st.write(tweet)

            st.divider()

        all_tweets = "\n\n".join(
            f"Tweet {i}: {tweet}"
            for i, tweet in enumerate(tweets, start=1)
        )

        st.download_button(
            label="Download all 10 tweets",
            data=all_tweets,
            file_name=f"{brand}_tweets.txt",
            mime="text/plain"
        )