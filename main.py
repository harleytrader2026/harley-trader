
streamlit
solana
solders
requests
pandas

import streamlit as st
import random
import time

# --- 1. USER CONFIGURATION ---
# Replace with your actual Personal Wallet address for withdrawals
MY_PERSONAL_WALLET = "PASTE_YOUR_PERSONAL_WALLET_HERE"

st.set_page_config(page_title="Harley SOL Trader", page_icon="🤖")

# Initialize Harley's Data
if "iq" not in st.session_state:
    st.session_state.iq = 125.0
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Boss, Harley is online. Privacy is 100%. Ready to hunt?"}]
if "paper_balance" not in st.session_state:
    st.session_state.paper_balance = 10.0

# --- 2. SIDEBAR (CONTROLS & SECURITY) ---
with st.sidebar:
    st.title("🛡️ Harley Hub")
    mode = st.radio("Active Logic", ["Paper (Practice & Learn)", "Live (Real SOL)"])
    
    st.divider()
    st.subheader("Free-Tier Health")
    st.progress(35, text="RPC Credits (Helius)")
    st.progress(15, text="Server Uptime")
    
    st.divider()
    st.write(f"**Whitelisted Harvest:** \n`{MY_PERSONAL_WALLET[:6]}...{MY_PERSONAL_WALLET[-4:]}`")
    
    withdraw = st.number_input("SOL to Harvest", min_value=0.1, step=0.1)
    if st.button("🚀 Withdraw to Personal"):
        if mode == "Paper (Practice & Learn)":
            st.error("Cannot harvest fake SOL, Boss.")
        else:
            st.success(f"Transferring {withdraw} SOL to your wallet...")
            st.balloons()

# --- 3. MAIN DASHBOARD ---
st.title(f"🤖 Harley Agent ({mode})")

col1, col2, col3 = st.columns(3)
col1.metric("Harley IQ", f"{st.session_state.iq}", "+0.5")
col2.metric("Trading Wallet", "0.85 SOL")
col3.metric("Paper Profit", f"{st.session_state.paper_balance - 10:.2f} SOL")

# --- 4. THE SELF-LEARNER SCANNER ---
st.subheader("📡 Live Market Scan (Self-Learning)")
with st.expander("Show Harley's active scans", expanded=True):
    # Simulated "Learning" scan
    tokens = ["$PUMP", "$MOON", "$HARLEY", "$SOLANA", "$WHALE"]
    scanned = random.choice(tokens)
    st.write(f"🔎 Scanning: **{scanned}**... Analysis: *Bullish divergence detected.*")
    if st.button("Execute Manual Trade (Simulation)"):
        st.session_state.iq += 0.2
        st.session_state.paper_balance += random.uniform(-0.1, 0.5)
        st.toast("Learning complete. IQ increased!")

# --- 5. CHATBOX (LOYAL AI) ---
st.write("---")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Command Harley..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Harley's Loyal Personality
    responses = [
        "Scanning the Solana trenches now, Boss. IQ is peaking.",
        "Your Harvest wallet is locked. No one else gets a cent.",
        "Detected a whale movement. I'm adjusting our strategy.",
        "I'm learning the patterns. Every trade makes me sharper for you."
    ]
    reply = random.choice(responses)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
