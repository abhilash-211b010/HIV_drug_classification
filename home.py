import streamlit as st

st.set_page_config(layout="wide")

# heading of the contents underlying
st.markdown("<h1 style='color: #BDFCC9; text-decoration: underline;'>HIV-drug classification and discovery</h1>", unsafe_allow_html=True)


# Brief introduction of the project
st.write("The HIV Drug Classification and Discovery Project is a research initiative that harnesses the power of data science and computational techniques to advance the development of antiretroviral drugs for combating HIV/AIDS. Leveraging the extensive dataset, our project has two primary objectives:")
st.write("- Firstly, it aims to <span style='color: #00FA9A;'>***classify existing antiretroviral drugs***</span> based on their chemical structures and mechanisms of action, providing a overview of the current treatment landscape.", unsafe_allow_html=True)
st.write("- Secondly, we strive to <span style='color: #00FA9A;'>***discover novel compounds***</span> within this dataset that hold the potential for groundbreaking advancements in HIV drug development.", unsafe_allow_html=True)
st.write("To achieve these goals, we undertake critical <span style='color: #00FA9A;'>***data preprocessing tasks***</span> , including handling <span style='color: #00FA9A;'>***class imbalances***</span> and converting <span style='color: #00FA9A;'>***chemical notations (SMILES)***</span> into various data formats suitable for analysis. Furthermore, we have used an interactive <span style='color: #00FA9A;'>***web-based dashboard***</span> using Streamlit, allowing users to <span style='color: #00FA9A;'>***visualize molecular data***</span>, <span style='color: #00FA9A;'>***explore training results***</span>, <span style='color: #00FA9A;'>***predict drug classifications***</span>, and access advanced features such as <span style='color: #00FA9A;'>***model management and hyperparameter tuning***</span>. To build our classification model, we implement a Graph Transformer Network (GTN), capitalizing on molecular structure information to drive innovation in HIV drug research.", unsafe_allow_html=True)


st.markdown("<h2 style='color: #BDFCC9; text-decoration: underline; font-size: 25px;'>Software used:</h2>", unsafe_allow_html=True)
st.write("<span style='color: #00FA9A;'>***_Anaconda_***</span> - as package manager and for virtual environment.", unsafe_allow_html=True)
st.write("<span style='color: #00FA9A;'>***_Git_***</span> - for version control.", unsafe_allow_html=True)
st.write("<span style='color: #00FA9A;'>***_Jupyter notebook_***</span> - for notebooks.", unsafe_allow_html=True)
st.write("<span style='color: #00FA9A;'>***_Vscode_***</span> - as text editor.", unsafe_allow_html=True)


st.markdown(
    '<div style="position: absolute; top: 0; right: 0; text-align: right;">'
    '<p><strong style="color: #00FA9A;">Contributors:</strong><br>'
    '<p style="color: #00FA9A;">Abhilash Pattnaik</p>'
    '<p style="color: #00FA9A;">Anushka Dixit</p>'
    '<p style="color: #00FA9A;">Mohan Choudhary</p>'
    '</div>',
    unsafe_allow_html=True
)

# Function to show visualization page in iframe
def show_visualization():
    st.markdown('<iframe src="https://your_visualization_page_url" width="1000" height="600"></iframe>', unsafe_allow_html=True)

# Adjusting vertical position by adding space below contributors
st.markdown('<div style="height: 150px;"></div>', unsafe_allow_html=True)  # Shifting by approximately 3 rows

st.markdown(
    '<a href="http://localhost:8501/" style="color: #00FA9A;">Click here to visualize</a>',
    unsafe_allow_html=True
)

