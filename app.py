import streamlit as st
from agent_teams import agent_team

st.set_page_config(page_title="AI Agent Team: Finance & Web Intelligence", layout="wide")

st.title("🤖 AI Agent Team: Finance & Web Intelligence")

query = st.text_input("Ask a question:", "Summarize analyst recommendations and share the latest news for NVDA")

if st.button("Run Agent"):
    with st.spinner("Agents are working..."):
        result = agent_team.run(query)

        # Try to extract the content from the last assistant message
        try:
            if hasattr(result, "messages") and result.messages:
                last = [m for m in result.messages if m.role == "assistant"]
                if last:
                    content = last[-1].content
                    st.markdown(content, unsafe_allow_html=True)
                else:
                    st.warning("No assistant message found.")
            elif hasattr(result, "markdown_text"):
                st.markdown(result.markdown_text, unsafe_allow_html=True)
            elif isinstance(result, str):
                st.markdown(result, unsafe_allow_html=True)
            else:
                st.text(str(result))  # Fallback
        except Exception as e:
            st.error(f"Error displaying result: {e}")

