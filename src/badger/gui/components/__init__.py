from pathlib import Path
from importlib import resources


style_path = str(resources.files(__package__) / "../stylesheet/matplot.style")

if Path(style_path).is_file():
    from matplotlib import pyplot
    pyplot.style.use(style_path)
