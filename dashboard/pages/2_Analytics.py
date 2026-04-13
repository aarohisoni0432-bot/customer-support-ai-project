import streamlit as st
import pandas as pd

st.set_page_config(page_title="Analytics Dashboard", page_icon="📊")

# title
st.title("📊 Analytics Dashboard")

st.markdown("### 📈 Customer Support Insights")

# sample data (you can later connect real data)
data = {
    "Category": ["technical", "billing", "refund", "account"],
    "Count": [45, 30, 20, 15]
}

df = pd.DataFrame(data)

# show table
st.markdown("### 🧾 Data Overview")
st.dataframe(df)

# bar chart
st.markdown("### 📊 Category Distribution")
st.bar_chart(df.set_index("Category"))

# pie chart
st.markdown("### 🥧 Category Share")
st.pyplot(df.set_index("Category").plot.pie(y="Count", autopct='%1.1f%%', figsize=(5,5)).figure)

# insights
st.markdown("### 💡 Insights")
st.info("""
- Most queries are technical issues
- Refund requests are moderate
- Account-related issues are lowest
""")