from src.FileConfig import Config, Files

CONFIG: Config = [
    # Add your file paths here.
    Files(
        client="dipomitsubishi-id", #800
        dashboard="202504/DB/dipomitsubishi-id.csv", 
        console="202504/console/dipomitsubishi-id.csv", 
        output="202504/merge/dipomitsubishi-id.csv",
        #rate=800 
    ),

]