import streamlit as st
import random

st.set_page_config(
    page_title="Divine Reiki Light Oracle",
    page_icon="✨",
    layout="centered"
)

# ==================== FULL CARD DATA ====================

meditations = [
    {"name": "Inner Stillness", "meaning": "A return to the quiet center within. True healing begins from deep inner calm."},
    {"name": "Grounded Presence", "meaning": "Being fully anchored in the present moment and connected to the Earth."},
    {"name": "Compassionate Heart", "meaning": "A gentle opening of the heart with kindness toward yourself and others."},
    {"name": "Releasing Worry", "meaning": "The conscious release of mental tension and future-focused anxiety."},
    {"name": "Grateful Awareness", "meaning": "A shift into appreciation for what already exists. Opens the heart to abundance."},
    {"name": "Forgiveness Flow", "meaning": "The gentle release of resentment, guilt, or emotional heaviness."},
    {"name": "Joyful Light", "meaning": "Reconnecting with lightness, playfulness, and the natural joy of being alive."},
    {"name": "Clear Seeing", "meaning": "Calm, non-reactive awareness and inner clarity. Cuts through confusion."},
    {"name": "Divine Connection", "meaning": "Strengthening the link between your personal energy and higher consciousness."},
    {"name": "Just for Today", "meaning": "Embracing Usui’s Five Precepts as a living daily practice."}
]

chakras = [
    {"name": "Root Chakra – Grounding", "meaning": "Your foundation, safety, and connection to the physical world."},
    {"name": "Sacral Chakra – Flow", "meaning": "Creativity, emotional flow, pleasure, and healthy relationships."},
    {"name": "Solar Plexus – Inner Fire", "meaning": "Personal power, confidence, will, and self-worth."},
    {"name": "Heart Chakra – Compassion", "meaning": "Love, compassion, forgiveness, and emotional balance."},
    {"name": "Throat Chakra – Expression", "meaning": "Authentic communication and speaking your truth."},
    {"name": "Third Eye – Clear Vision", "meaning": "Intuition, insight, mental clarity, and spiritual perception."},
    {"name": "Crown Chakra – Divine Connection", "meaning": "Spiritual connection and unity with the Divine."},
    {"name": "Earth Star – Deep Grounding", "meaning": "Your energetic connection to the Earth and ancestral roots."},
    {"name": "Hara – Life Force Center", "meaning": "Your vital life force, willpower, and inner strength."},
    {"name": "Soul Star – Higher Light", "meaning": "Connection to your Higher Self and spiritual purpose."}
]

symbols = [
    {"name": "Choku Rei (CKR) – Power Symbol", "meaning": "Focuses, protects, and amplifies energy. Strengthens your field and intention."},
    {"name": "Sei He Ki (SHK) – Mental & Emotional Healing", "meaning": "Purifies and releases worry, fear, anger, and old emotional patterns."},
    {"name": "Hon Sha Ze Sho Nen (HSZSN) – Distant Healing", "meaning": "The bridge across time and space. Sends healing to past, future, or others."},
    {"name": "Dai Ko Myo (DKM) – Master Symbol", "meaning": "Great shining light of enlightenment and deep spiritual transformation."},
    {"name": "Raku – Grounding & Sealing", "meaning": "Grounds and seals energy work. Brings healing deep into the body."},
    {"name": "Tibetan Dai Ko Myo", "meaning": "Powerful, grounded spiritual energy for deep karmic or ancestral work."},
    {"name": "Fire Serpent (Tibetan)", "meaning": "Rising kundalini energy that awakens life force and clears blockages."},
    {"name": "Shika Sei Ki", "meaning": "Brings emotional balance and harmony to the heart."},
    {"name": "Halu", "meaning": "Symbol of truth and protection. Reveals what has been hidden with compassion."},
    {"name": "Harth", "meaning": "Heart healing and compassion. Opens the heart to give and receive love."},
    {"name": "Rama", "meaning": "Manifestation and connection to the Earth. Grounds intentions into reality."},
    {"name": "Gnosa", "meaning": "Knowledge and inner wisdom. Helps access higher guidance and understanding."},
    {"name": "Iava", "meaning": "Karmic clearing and release across lifetimes. Dissolves old soul contracts."},
    {"name": "Shanti", "meaning": "Peace and harmony. Brings deep calm after intense healing work."},
    {"name": "Kriya", "meaning": "Action and transformation. Turns insight into aligned movement."}
]

treatment = [
    {"name": "Hands-On Self Treatment", "meaning": "Direct physical application of Reiki to your own body."},
    {"name": "Distant / Proxy Healing", "meaning": "Sending Reiki across time, space, or to others (including past/future self)."},
    {"name": "Emotional Body Release", "meaning": "Working directly with feelings and stored emotional patterns."},
    {"name": "Mental Body Clearing", "meaning": "Clearing thought patterns, mental fog, and limiting beliefs."},
    {"name": "Aura Field Cleansing", "meaning": "Sweeping, clearing, and strengthening your energetic field."},
    {"name": "Energy Cord Cutting", "meaning": "Releasing unhealthy energetic attachments and cords."},
    {"name": "Symbol Activation Practice", "meaning": "Intentionally working with Reiki symbols in a focused, ritual way."},
    {"name": "Chakra Balancing Sequence", "meaning": "Structured, sequential balancing of the energy centers."},
    {"name": "Reiki + Meditation Fusion", "meaning": "Combining Reiki with deep meditative stillness."},
    {"name": "Breath & Energy Flow Work", "meaning": "Using conscious breathing to move and amplify Reiki."},
    {"name": "Daily Precept Integration", "meaning": "Living one of Usui’s Five Precepts as an active daily healing practice."}
]

crystals = [
    {"name": "Clear Quartz – Master Amplifier", "meaning": "Amplifies and clarifies your entire 5-card pattern. Makes everything stronger and clearer."},
    {"name": "Amethyst – Spiritual Connection & Calm", "meaning": "Deepens meditation and opens crown/third eye. Excellent for spiritual guidance."},
    {"name": "Rose Quartz – Heart Healing & Compassion", "meaning": "Softens and opens the heart. Perfect for emotional healing and self-compassion."},
    {"name": "Black Tourmaline – Protection & Grounding", "meaning": "Strong protection and grounding. Absorbs negativity and anchors your energy."},
    {"name": "Selenite – Cleansing & Divine Light", "meaning": "Pure cleansing and raising of vibration. Clears your space and energy field."},
    {"name": "Citrine – Joy & Personal Power", "meaning": "Brings joy, confidence, and manifestation energy to the solar plexus."},
    {"name": "Labradorite – Intuition & Aura Shield", "meaning": "Strengthens intuition and protects your aura. Excellent after deep work."},
    {"name": "Carnelian – Vitality, Courage & Creative Fire", "meaning": "Ignites courage, vitality, and creative action. Helps you move forward."},
    {"name": "Tiger’s Eye – Focused Will & Grounded Action", "meaning": "Brings focus, protection, and grounded courage. Helps you take clear action."},
    {"name": "Moonstone – Emotional Flow & Divine Feminine", "meaning": "Supports gentle emotional flow and connection to inner wisdom."},
    {"name": "Lapis Lazuli – Truth & Higher Communication", "meaning": "Opens throat and third eye. Helps you speak and receive truth with clarity."},
    {"name": "Green Aventurine – Heart Opening & Gentle Growth", "meaning": "Brings gentle growth, opportunity, and heart-centered forward movement."},
    {"name": "Red Jasper – Grounding, Vitality & Life Force", "meaning": "Deep grounding and restoration of physical/energetic stamina."},
    {"name": "Malachite – Heart Transformation & Prosperity", "meaning": "Powerful transformation and emotional healing. Supports prosperity from inner alignment."}
]

# ==================== APP INTERFACE ====================

st.title("✨ Divine Reiki Light Oracle")
st.subheader("5-Point Star Healing Draw • Zen Balance Box")

st.markdown("""
This oracle was created exclusively for Zen Balance Box by Zulekha Mir (Level 2 Reiki practitioner).  
Enter your intention below, then draw your pattern. Each card is drawn intentionally from its suit to create a coherent healing message.
""")

intention = st.text_input(
    "What is your intention for this draw?",
    placeholder="I intend to release old emotional patterns and step into my power with clarity..."
)

if st.button("Draw My 5-Point Reiki Pattern", type="primary", use_container_width=True):
    if not intention.strip():
        st.warning("Please enter an intention to begin your draw.")
    else:
        st.success("Your pattern has been drawn with clear intention.")

        # Random draw (one from each suit)
        draw = {
            "Meditation (Top)": random.choice(meditations),
            "Chakra Focus (Left)": random.choice(chakras),
            "Reiki Symbol (Right)": random.choice(symbols),
            "Treatment (Bottom Left)": random.choice(treatment),
            "Crystal Ally (Bottom Right)": random.choice(crystals)
        }

        st.markdown("### Your 5-Point Star Pattern")

        # Top - Meditation
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            card = draw["Meditation (Top)"]
            st.markdown(f"**🔝 Top – Meditation**  \n**{card['name']}**  \n*{card['meaning']}*")

        # Left + Right
        col1, col2, col3 = st.columns(3)
        with col1:
            card = draw["Chakra Focus (Left)"]
            st.markdown(f"**◀ Left – Chakra**  \n**{card['name']}**  \n*{card['meaning']}*")
        with col3:
            card = draw["Reiki Symbol (Right)"]
            st.markdown(f"**▶ Right – Symbol**  \n**{card['name']}**  \n*{card['meaning']}*")

        # Bottom Left + Bottom Right
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            card = draw["Treatment (Bottom Left)"]
            st.markdown(f"**↙ Bottom Left – Treatment**  \n**{card['name']}**  \n*{card['meaning']}*")
        with col3:
            card = draw["Crystal Ally (Bottom Right)"]
            st.markdown(f"**↘ Bottom Right – Crystal**  \n**{card['name']}**  \n*{card['meaning']}*")

        st.markdown("---")

        # How to work with this pattern
        st.markdown("### How to Work With This Pattern")
        st.markdown("""
        1. Cleanse your space with Selenite, Palo Santo, or Florida Water.
        2. Place your **Crystal Ally** on the chakra area indicated or in the center of your altar.
        3. Activate the **Reiki Symbol** three times over your hands or the area of focus.
        4. Follow the guidance of the **Treatment** card for 10–15 minutes.
        5. End by placing both hands on the crystal and stating your intention out loud.
        """)

        st.caption("This is for reflection, meditation, and spiritual wellness only. It is not a substitute for medical or professional advice. Reiki healing is best received in person from a trained practitioner.")

st.markdown("---")
st.caption("© 2026 Zen Balance Box. All rights reserved. Original work created exclusively for Zen Balance Box.")