import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import io
import base64


def generate_chart(df):

    if df is None or df.empty:
        return None
    
    if df.shape[1] < 2:
        return None

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    plt.figure(figsize=(8,4))
    plt.bar(x.astype(str), y)

    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    chart = base64.b64encode(img.getvalue()).decode()

    plt.close()

    return chart