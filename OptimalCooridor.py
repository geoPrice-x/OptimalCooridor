import arcpy
from arcpy.sa import *
from arcpy.management import *


def OptimalCooridor(ws, highway, output):
    
    # set environmental variables
    arcpy.env.workspace = ws

    # allow overwrites
    arcpy.env.overwriteOutput = True

    # check out licenses
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

###################################################################

    # distance accumulation from highways
    arcpy.AddMessage("Running Distance Accumulation...")
    HighwayDist = DistanceAccumulation(in_source_data = highway, distance_method='PLANAR')
    arcpy.AddMessage("Distance Accumulation completed.")

    # reclassify highway distance raster
    arcpy.AddMessage("Reclassifying raster...")
    HD_Max = GetRasterProperties(HighwayDist, "MAXIMUM")
    Reclass1 = Reclassify(HighwayDist, "Value", f"0 250 1;250 1000 2;1000 5000 3;5000 10000 4;10000 {HD_Max} 5", "DATA")
    Reclass1.save(output)
    arcpy.AddMessage("Completed.")

###################################################################
    
    


    return


if __name__ == "__main__":

    ws = arcpy.GetParameterAsText(0)
    highway = arcpy.GetParameterAsText(1)
    output = arcpy.GetParameterAsText(2)

    OptimalCooridor(ws, highway, output)