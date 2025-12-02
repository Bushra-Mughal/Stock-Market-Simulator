#  Stock-exchange market (secondary shares) simulator dashboard
# TAG LINE: trade in real-time share market!

# copy and run on terminal:
### streamlit run "Stock Market Simulator\dashboard.py"

import streamlit as st
# import StockMarket_class as sm_class
from StockMarket_class import stock_market

# === Simple STREAMLIT DASHBOARD ===
st.set_page_config(page_title="Stock Market Simulator", layout="centered")
st.title("Stock Market Simulator")
st.markdown("**Trade in real-time share market!**")

# Initialize session state
if 'sm' not in st.session_state:
    st.session_state.sm = stock_market()

sm = st.session_state.sm

# Sidebar Menu
menu = st.sidebar.selectbox("Menu", [
    "1. View Stock Market",
    "2. Edit Your Shares",
    "3. Stock Market Guide"
])

# === 1. View Stock Market ===
if menu == "1. View Stock Market":
    st.subheader("Real-Time Stock Market")
    st.code(sm.show_stock_market())

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sell Stock"):
            st.session_state.action = "sell"
    with col2:
        if st.button("Buy Stock"):
            st.session_state.action = "buy"

    if 'action' in st.session_state:
        if st.session_state.action == "sell":
            name = st.text_input("Enter stock name to sell:")
            if st.button("Confirm Sell"):
                msg = sm.sell_stock(name)
                st.success(msg)
                del st.session_state.action

        elif st.session_state.action == "buy":
            num = st.number_input("Enter stock number (1-6)", min_value=1, max_value=6, step=1)
            if st.button("Confirm Buy"):
                msg = sm.buy_stock(int(num))
                st.success(msg)
                del st.session_state.action

# === 2. Edit Your Shares ===
elif menu == "2. Edit Your Shares":
    st.subheader("Your Portfolio")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Last Sold Stock"):
            st.info(sm.show_last_sold_stock())
    with col2:
        if st.button("Show Bought Stocks"):
            st.code(sm.show_buy_stocks())

# === 3. Stock Market Guide ===
elif menu == "3. Stock Market Guide":
    st.subheader("Stock Market 101")
    st.write(sm.stock_market_info())

# Footer
st.markdown("---")
st.markdown("**Thanks for using the simulator!**")

##NOTE: WE DONT NEED A 'MODULE GUARD' IN STREAMLIT