
import streamlit as st
import json

# Load picks
with open("picks.json") as f:
    picks = json.load(f)

st.title("Big Raf Bets™ — Model Picks")

st.markdown("### ✅ Verified Model Picks (Sorted by Confidence Score)")

# Display picks
for pick in sorted(picks, key=lambda x: -x["confidence"]):
    st.markdown(f"**{pick['player']}** — {pick['bet_type']} **{pick['direction']}** {pick['line']} ({pick['odds']}) {pick['emoji']} — Confidence: {pick['confidence']}%")
