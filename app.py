import gradio as gr
from functions.analysisTeacher import analysis_teacher
from functions.dataAnalysis import analysis_data_match


def combined_analysis():
    analysis_data_match()
    analysis_teacher()
    return "Analysis Process Done!"

demo = gr.Interface(
    fn=combined_analysis,
    inputs=None,
    outputs="text",
    title="Combined Sentiment and Emotion Match Analysis",
    description="Analyze the sentiment and emotions of student comments and the matches between the emotions of students and teachers.",
    api_name="/combined_analysis"
)
if __name__ == "__main__":
    demo.launch(server_port=7864,root_path="/analysis_data_edulytics")