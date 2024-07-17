import streamlit as st
import base64
from pathlib import Path
import tempfile
import streamlit.components.v1 as comp
import moviepy.editor as mp
import os
import whisper
from deep_translator import GoogleTranslator
import whisper.tokenizer
import nltk
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

# Custom footer
def footer():
    style = """
    <style>
    a:link, a:visited {
        color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness */
        background-color: transparent;
        text-decoration: none;
    }

    a:hover, a:active {
        color: #0283C3; /* theme's primary color */
        background-color: transparent;
        text-decoration: underline;
    }

    #page-container {
        position: relative;
        min-height: 10vh;
    }

    footer {
        visibility: hidden;
    }

    .footer {
        display: flex;
        justify-content: end;
        align-items: center;
        text-align: center;
        position: relative;
        left: 0;
        top: 230px;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #808080; /* theme's text color hex code at 50 percent brightness */
        text-align: left; /* you can replace 'left' with 'center' or 'right' if you want */
    }

    .pylogo_footer {
        height: 12px;
    }

    .slogo_footer {
        height: 10px;
    }
    </style>
    """

    st.markdown(style, unsafe_allow_html=True)

    footer_content = div(
        _class='footer',
        style = """
            display: flex;
            justify-content: end;
            align-items: center;
            text-align: center;
            position: relative;
            left: 0;
            top: 230px;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #808080; /* theme's text color hex code at 50 percent brightness */
            text-align: left; /* you can replace 'left' with 'center' or 'right' if you want */
        """
    )(
        p(
            style='font-size: 0.875em;'
        )(
            "Made with: ",
            a(
                href="https://www.python.org/",
                target="_blank",
                style='display: inline; text-align: left;'
            )("Python 3.9 "),
            img(
                src="https://i.imgur.com/ml09ccU.png",
                _class="pylogo_footer",
                style='height: 12px;'
            ),
            " & ",
            a(
                href="https://streamlit.io/",
                target="_blank",
                style='display: inline; text-align: left;'
            )("Streamlit "),
            img(
                src="https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png",
                _class="slogo_footer",
                style='height: 10px'
            ),
            br(),
            "by: ",
            a(
                href="https://github.com/AlgorithmicPV",
                target="_blank",
                style='display: inline; text-align: left;'
            )("AlgorithmicPV")
        )
    )

    page_container = div(
        id='page-container'
    )(footer_content)

    st.markdown(str(page_container), unsafe_allow_html=True)

st.set_page_config(
    page_title="VidTranslate | App",
    page_icon="static\\vidtranlate.png",
    layout="wide",
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        margin-top: 1rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Main interface of the app
def main():
    style = """
    <style>
    #MainMenu {
    visibility: hidden;
    }

    footer {
    visibility: hidden;
    }

    header {
    visibility: hidden;
    }

    .title{
    color: yellow;
    }

    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

    def img_to_base64(img_path):
        with open(img_path, "rb") as img_file:
            img_bytes = img_file.read()
            encoded = base64.b64encode(img_bytes).decode()
        return encoded


    def header_img_to_html(img_path):
        encoded_img = img_to_base64(img_path)
        custom_css = """
        <style>
        [data-testid="stAppViewContainer"] > .main {
            border: 0px solid rgba(100, 100, 100, 1);
            background:
                radial-gradient(
                    circle,
                    #0E1117,
                    #0E1117 80%
                ),
                linear-gradient(
                    45deg,
                    #1F4068,
                    #E43F5A,
                    #1F4068,
                    #E43F5A
                );
            background-blend-mode: normal;
        }
        .header-container {
            display: flex;
            align-items: center;
        }
        .logo-img {
            width: 50px;  /* Adjust width as needed */
            height: auto; /* Maintain aspect ratio */
            margin-right: 10px; /* Adjust spacing between image and text */
            border-radius: 50%; /* Rounded corners for circular shape */
        }
        .app-title {
            font-size: 24px;
            font-weight: bold;
            height: 24px;
        }
        </style>
        """

        img_html = f"""
        <nav class="header-container">
            <img src="data:image/png;base64,{encoded_img}" class="logo-img">
            <p class="app-title">Vidtranslate</p>
        </nav>
        """
        return custom_css + img_html

    # Get the HTML content with embedded CSS
    html_content = header_img_to_html('static\\vidtranlate.png')

    # Display the HTML with embedded CSS in Streamlit
    st.markdown(html_content, unsafe_allow_html=True)

    html_p = """
        <div class="txt_part">
            <p class="head">Upload video, get subtitles translated fast!</p>
            <p class="txt">
            Unlock the power of your videos with our Video Transcript Translator! Extract and translate transcripts into English effortlessly. Ideal for creators, educators, and professionals seeking quick, accurate translations to reach a broader audience.</p>
        </div>
        """
    html_p_css = """
        <style>
        .head{
        font-size:65px;
        text-align:center;
        text-wrap: wrap;
        width:100%;
        font-weight: bold;
        }

        .txt{
        text-align:center;
        color: gainsboro;
        width:60%;
        text-wrap:wrap;
        }

        .txt_part{
        display:flex;
        justify-content:center;
        align-items:center;
        width:100%;
        flex-direction: column;
        margin-top: 5%;
        }

        div[data-testid="stButton"]
        {
            text-align: center;
            width:fit;
            display:flex;
            justify-content:center;
            align-items:center;
        }
        """

    st.markdown(html_p_css, unsafe_allow_html=True)
    st.markdown(html_p, unsafe_allow_html=True)

    
    if 'uploaded_file' not in st.session_state:
        st.session_state.uploaded_file = None

    if st.button("Upload !"):
        st.session_state.page = "upload"

    comp.html("""
    <script>
        const elements = window.parent.document.querySelectorAll('.stButton > button');
        elements[0].style.backgroundColor = "#0E1117";
        elements[0].style.color = "#F5730C";
        elements[0].style.borderColor = "#F5730C";

        elements[0].style.height= "60px";
        elements[0].style.width= "280px";      
              
        elements[0].addEventListener("mouseover", function() {
            this.style.backgroundColor = "#F5730C";
            this.style.color = "#0E1117";  
            this.style.borderColor = "#0E1117"; // New hover border color
        });
        elements[0].addEventListener("mouseout", function() {
            this.style.backgroundColor = "#0E1117"; // Restore original background color
            this.style.color = "#F5730C"; // Restore original text color
            this.style.borderColor = "#F5730C"; // Restore original border color
        });
    </script>
    """, height=0, width=0)

    if 'page' in st.session_state and st.session_state.page == "upload":
        upload_page()

nltk.download('punkt')

#video upload part
def upload_page():
    st.header("Upload your video file")

    languages = whisper.tokenizer.LANGUAGES
    language_map = {name: code for code, name in languages.items()}
    language_options = ["Auto"] + list(language_map.keys())

    # Language selection dropdown
    language_option = st.selectbox(
        "Pick the language of the video",
        language_options,  # Add more languages as needed
        index=0,
        help="Select the language spoken in the video",
    )

    # File uploader for video files
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary directory
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        with st.spinner('Preparing...'): # Loading cycle
            try:
                video = mp.VideoFileClip(temp_file_path)
                name = os.path.basename(temp_file.name)
                base_name = os.path.splitext(name)[0]
                audio_filename = f"{base_name}_extracted_audio.mp3"
                video.audio.write_audiofile(audio_filename)

                model = whisper.load_model("medium")
                result = model.transcribe(audio_filename, fp16=False)
                transcription = result["text"]

                vtt_filename = f"{base_name}_subtitles.vtt"

                with open(vtt_filename, "w", encoding="utf-8") as subtitles:
                    subtitles.write("WEBVTT\n\n")
                    for i, segment in enumerate(result['segments']):
                        start, end = segment['start'], segment['end']
                        start_minutes, start_seconds = divmod(int(start), 60)
                        start_milliseconds = int((start - int(start)) * 1000)
                        end_minutes, end_seconds = divmod(int(end), 60)
                        end_milliseconds = int((end - int(end)) * 1000)
                        subtitles.write(f"00:{start_minutes:02}:{start_seconds:02}.{start_milliseconds:03} --> 00:{end_minutes:02}:{end_seconds:02}.{end_milliseconds:03}\n")
                        subtitles.write(f"{segment['text'].strip()}\n\n")

                if language_option == "Auto":
                    source_lang = 'auto'
                else:
                    source_lang = language_option.lower()

                with open(vtt_filename, "r", encoding="utf-8") as file:
                    vtt_content = file.read()
                segments = vtt_content.split('\n\n')
                translated_segments = []
                text_to_translate = ""

                for segment in segments:
                    if len(text_to_translate + segment) > 5000:
                        translated_text = GoogleTranslator(source=source_lang, target='en').translate(text_to_translate)
                        translated_segments.append(translated_text)
                        text_to_translate = segment + '\n\n'
                    else:
                        text_to_translate += segment + '\n\n'

                if text_to_translate:
                    translated_text = GoogleTranslator(source=source_lang, target='en').translate(text_to_translate)
                    translated_segments.append(translated_text)
                translated_vtt_filename = f"translated_{vtt_filename}"
                with open(translated_vtt_filename, "w", encoding="utf-8") as file:
                    file.write('\n\n'.join(translated_segments))

                st.success('Done!')
                st.video(temp_file_path, subtitles=translated_vtt_filename)

                vtt_contents = vtt_content
                st.download_button("Download Original Transcript", vtt_contents)

                with open(translated_vtt_filename, "r", encoding="utf-8") as file:
                    vtt_content_translate = file.read()

                vtt_contents_translated = vtt_content_translate
                st.download_button("Download Translated Transcript", vtt_contents_translated)

            except Exception as e:
                st.error(f"An error occurred: {e}")
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)
                if os.path.exists(audio_filename):
                    os.remove(audio_filename)
                if os.path.exists(vtt_filename):
                    os.remove(vtt_filename)
                if os.path.exists(translated_vtt_filename):
                    os.remove(translated_vtt_filename)
               
if __name__ == "__main__":
    main()
    footer()


# by AlgorithmicPV
# https://github.com/AlgorithmicPV 