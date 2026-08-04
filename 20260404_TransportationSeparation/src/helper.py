import pickle
import json

def write_pickle(file_path, object):
    with open(file_path, 'wb') as fp:
        pickle.dump(object, fp)


def read_pickle(file_path):
    with open(file_path, 'rb') as f:  # notice the r instead of w
        pickled_object = pickle.load(f)
    return pickled_object

def write_json(file_path, object):
    with open(file_path, "w") as f:
        json.dump(object, f)

def read_json(file_path):
    with open(file_path, "r") as f:
        json_file = json.load(f)
    return json_file

def add_attribution(file_path):
    ATTRIBUTION_HTML = """
    <div style="
        position: absolute; 
        bottom: 0; 
        right: 0; 
        background: rgba(255, 255, 255, 0.85); 
        padding: clamp(2px, 0.6vw, 4px) clamp(4px, 1vw, 8px); 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
        font-size: clamp(8px, 1vw, 11px); 
        color: #333; 
        z-index: 99999;
        border-top-left-radius: 4px;
        box-shadow: 0 0 4px rgba(0,0,0,0.15);
        pointer-events: auto;
        white-space: normal;
        word-break: break-word;
        max-width: 95vw;
        text-align: right;
    ">
        Esri, Maxar, Earthstar Geographics, and the GIS User Community
    </div>
    </body>
    """
 
    # Read the file, inject the overlay block right before the closing body tag, and save
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Swap out the closing body tag with our attribution + closing tag
    patched_html = html_content.replace("</body>", ATTRIBUTION_HTML)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(patched_html)
    print("Added Esri attribution text")


def upgrade_widget_in_html(file_path):
    """Upgrade the stylesheet retroactively to use
    widget v.9.3 which has PopupWidget

    Args:
        file_path (str): Path to your HTML file
    """
    # Read the generated HTML file
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Force the jupyter-widget script to v9.3+ where PopupWidget exists
    html_content = html_content.replace(
        "https://cdn.jsdelivr.net/npm/@deck.gl/jupyter-widget@~9.2.*/dist/index.js",
        "https://cdn.jsdelivr.net/npm/@deck.gl/jupyter-widget@^9.3.0/dist/index.js"
    )

    widgets_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@deck.gl/widgets@^9.3.0/dist/stylesheet.css" />\n</head>'
    html_content = html_content.replace("</head>", widgets_css)

    # Save the patched file back out
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("CDN version bumped to 9.3")

def add_network_legend(file_path):
    LEGEND_HTML = """
    <!-- Floating Responsive Network Legend Layer -->
    <div style="
        position: absolute;
        bottom: clamp(28px, 5vw, 42px); /* Pushes legend above the ~22px tall attribution bar */
        right: clamp(8px, 2vw, 16px);
        background-color: rgba(255, 255, 255, 0.95);
        padding: clamp(6px, 1.5vw, 12px) clamp(8px, 2vw, 16px);
        border-radius: 6px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: clamp(10px, 1.2vw, 13px);
        color: #333;
        z-index: 99999;
        pointer-events: auto;
        width: clamp(100px, 20vw, 160px);
    ">
        <div style="font-weight: bold; margin-bottom: clamp(4px, 1vw, 8px); border-bottom: 1px solid #eee; padding-bottom: clamp(2px, 0.5vw, 4px);">
            Network Layers
        </div>
        
        <!-- Red Line Item -->
        <div style="display: flex; align-items: center; margin-bottom: clamp(3px, 0.8vw, 6px);">
            <div style="width: clamp(14px, 2.5vw, 24px); height: clamp(2px, 0.4vw, 4px); background-color: #FF0000; margin-right: clamp(6px, 1vw, 10px); border-radius: 2px; flex-shrink: 0;"></div>
            <span>Roads</span>
        </div>
        
        <!-- Green Line Item -->
        <div style="display: flex; align-items: center;">
            <div style="width: clamp(14px, 2.5vw, 24px); height: clamp(2px, 0.4vw, 4px); background-color: #00FF00; margin-right: clamp(6px, 1vw, 10px); border-radius: 2px; flex-shrink: 0;"></div>
            <span>Pedestrian/Bike Paths</span>
        </div>
    </div>
    </body>
    """

    # Read the file, inject the overlay block right before the closing body tag, and save
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Swap out the closing body tag with our legend + closing tag
    patched_html = html_content.replace("</body>", LEGEND_HTML)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(patched_html)
        
    print("Injected network layer legend into the map layout")

    