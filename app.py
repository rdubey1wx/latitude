import streamlit as st
import time

def main():
    # Set page config
    st.set_page_config(page_title="Snapshot Reporting", layout="wide")

    # Custom CSS for styling
    st.markdown(
        """
        <style>
            .ribbon {
                background-color: #2596be; /* APRA logo blue */
                color: white;
                padding: 15px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
                border-radius: 8px;
                margin-bottom: 20px;
                width: 100%;
                box-sizing: border-box;
            }
            .menu-item {
                display: flex;
                align-items: center;
                justify-content: flex-start;
                background-color: #4CAF50;
                color: white;
                padding: 15px 25px;
                border-radius: 8px;
                text-align: left;
                font-size: 18px;
                font-weight: bold;
                transition: all 0.3s;
                cursor: pointer;
                width: 100%;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
                position: relative;
                margin-bottom: 10px;
            }
            .menu-item:hover {
                background: linear-gradient(135deg, #45a049, #1E6F43);
                transform: scale(1.05);
                box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
            }
            .menu-item::before {
                content: "";
                position: absolute;
                left: -15px;
                top: 50%;
                transform: translateY(-50%);
                width: 0;
                height: 0;
                border-left: 12px solid blue;
                border-top: 12px solid transparent;
                border-bottom: 12px solid transparent;
            }
            .menu-content {
                margin-top: 15px;
                padding: 15px;
                border-radius: 8px;
                background: #f8f8f8;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
                font-size: 16px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar
    st.sidebar.image("apra_logo.png", width=200)
    st.sidebar.title("Navigation")
    st.sidebar.write("Choose an option from the menu.")

    # Main Title with Ribbon
    st.markdown("<div class='ribbon'>Welcome to APRA NDP Platform</div>", unsafe_allow_html=True)

    # Menu Options in Sidebar
    menu_options = {
        "Add Snapshot Record": "This section allows you to add a new snapshot record.",
        "Display Snapshot Records": "This section allows you to add a new snapshot record.",
        "Choose the Model to Run": "Select a model to process your data.",
        "Display the Result": "View the results of your processed data.",
        "Run the Model": "Execute the selected model on the dataset."
    }

    selected_option = st.session_state.get('selected_option', list(menu_options.keys())[0]) # initialize session state

    for label, content in menu_options.items():
        if st.sidebar.button(label, key=label, use_container_width=True, on_click=lambda l=label: st.session_state.update({'selected_option': l})):
            pass

    # Display Content based on Selected Option
    st.markdown(f"<div class='menu-content'>{menu_options[selected_option]}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()