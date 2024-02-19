import arcpy
from arcpy.sa import *


def OptimalCooridor(highway, scratch):
    
    # allow overwrites
    arcpy.env.overwriteOutput = False

    # check out licenses
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageAnalyst")
    arcpy.CheckOutExtension("3D")

    # distance accumulation from highways
    HighwayDist = fr"{scratch}\HighwayDist"
    Dist_Accum = arcpy.sa.DistanceAccumulation(in_source_data= highway, distance_method='PLANAR')
    Dist_Accum.save(HighwayDist)

    # reclassify highway distance raster
    HighwayDistReclass = fr"{scratch}\HighDistRec"
    HD_Max = arcpy.management.GetRasterProperties(HighwayDist, "MAXIMUM")
    Reclass1 = arcpy.sa.Reclassify(HighwayDist, "Value", f"0 250 1;250 1000 2;1000 5000 3;5000 10000 4;10000 {HD_Max} 5", "DATA")
    Reclass1.save(HighwayDistReclass)



    return


if __name__ == "__main__":

    scratch = arcpy.GetParameterAsText(0)
    highway = arcpy.GetParameterAsText(1)

    OptimalCooridor(highway, scratch)