import plotly.graph_objects as go


def get_donut_of_topics(clusters_to_show):
    NUM_CLUSTERS_TO_USE = len(clusters_to_show)
    if NUM_CLUSTERS_TO_USE > 20:
        NUM_CLUSTERS_TO_USE = 20

    sum = 0
    for cluster in clusters_to_show[:NUM_CLUSTERS_TO_USE]:
        sum += len(cluster)

    percentages = []
    for cluster in clusters_to_show:
        percentages.append((len(cluster)/sum)*100.0)

    labels = [f"Topic{i}" for i in range(1, NUM_CLUSTERS_TO_USE)]
    values = percentages

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(width = 720, height = 720)

    return fig