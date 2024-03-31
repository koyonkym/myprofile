from django.shortcuts import render
from .models import ToeicScore
import plotly.graph_objects as go
import pandas as pd


def index(request):
    scores = ToeicScore.objects.all()
    plot_div = generate_plot_div(scores)
    return render(request, "single_page/index.html", {"plot_div": plot_div})


def generate_plot_div(queryset):
    if queryset.exists():
        df = pd.DataFrame(list(queryset.values()))

        df['test_date'] = pd.to_datetime(df['test_date'])
        df.set_index('test_date', inplace=True)

        # Apply the mapping function to a DataFrame column
        df['s_predicted_score'] = df['total_score'].apply(map_speaking_score)
        df['w_predicted_score'] = df['total_score'].apply(map_writing_score)

        # Create traces for listening and reading (first y-axis)
        trace1 = go.Scatter(x=df.index, y=df['l_score'], opacity=0.8, mode='lines+markers', name='L', yaxis='y1', line=dict(color='#3366CC'))
        trace2 = go.Scatter(x=df.index, y=df['r_score'], opacity=0.8, mode='lines+markers', name='R', yaxis='y1', line=dict(color='#109618'))

        # Create traces for speaking and writing (second y-axis)
        trace3 = go.Scatter(x=df.index, y=df['s_predicted_score'], opacity=0.8, mode='lines+markers', name='S', yaxis='y2', line=dict(color='#FF9900', dash='dot'))
        trace4 = go.Scatter(x=df.index, y=df['w_predicted_score'], opacity=0.8, mode='lines+markers', name='W', yaxis='y2', line=dict(color='#990099', dash='dot'))

        # Define layout with two y-axes
        layout = go.Layout(
            title='TOEIC Score Over Time',
            xaxis=dict(
                title='Date'
            ),
            yaxis=dict(
                title='Listening & Reading Scores', # First y-axis title
                side='left' # Position the axis on the left side
            ),
            yaxis2=dict(
                title='Predicted Speaking & Writing Scores', # Second y-axis title
                overlaying='y', # Overlay the axis on top of the first one
                side='right' # Position the axis on the right side
            ),
            legend=dict(
                x=1,
                y=1,
                xanchor='right',
                yanchor='bottom',
                orientation='h', # Horizontal orientation
            ),
            template='none'
        )

        # Create figure with traces and layout
        fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

        fig.update_layout(modebar_remove=['zoom', 'pan', 'select', 'zoomIn', 'zoomOut', 'autoScale', 'lasso'])

        # Convert the Plotly figure to HTML
        plot_div = fig.to_html(full_html=False)

        return plot_div
    else:
        return None


# Define the mapping function
def map_speaking_score(score):
    assert 10 <= score <= 990, "Scores must be between 10 and 990"
    if score >= 950:
        return 170
    elif score >= 880:
        return 160
    elif score >= 815:
        return 150
    elif score >= 745:
        return 140
    elif score >= 675:
        return 130
    elif score >= 605:
        return 120
    elif score >= 535:
        return 110
    elif score >= 465:
        return 100
    elif score >= 395:
        return 90
    elif score >= 350:
        return 80
    else:
        return 70

def map_writing_score(score):
    assert 10 <= score <= 990, "Scores must be between 10 and 990"
    if score >= 960:
        return 180
    elif score >= 890:
        return 170
    elif score >= 825:
        return 160
    elif score >= 760:
        return 150
    elif score >= 695:
        return 140
    elif score >= 625:
        return 130
    elif score >= 560:
        return 120
    elif score >= 495:
        return 110
    elif score >= 425:
        return 100
    elif score >= 360:
        return 90
    elif score >= 350:
        return 80
    else:
        return 70