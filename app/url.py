from .config import Config

def form_url(api_call, *args):
        """Forms an api call url from the base url and the given arguments
        
        Arguments:
            api_call {string} -- the function to take the arguments and 
            arguments {string} -- the string to be appended to the base url
        """
        base_url = Config.WEB['URL']
        arguments = api_call(*args).replace(" ", "%20")
        return base_url+arguments

class APICall():
    """Collection of api call functions"""

    class MapResources():
        @staticmethod
        def get_all_maps():
            """This API returns all maps"""
            return '/config/v1/maps'

        @staticmethod
        def get_count_of_all_map_elements():
            """This API provides count of campuses, buildings and floors"""
            return "/config/v1/maps/count"

        @staticmethod
        def get_all_building_names(campusName=''):
            """This API provides a list of all Buildings"""
            return "/config/v1/maps/building/list%s" % campusName

        @staticmethod
        def clients_history(locatedAfterTime, locatedBeforeTime):
            """Extract small chunks of data by specifying parameters locatedAfterTime and locatedBeforeTime (both in milliseconds)"""
            return "/location/v1/history/clients?locatedAfterTime={}&locatedBeforeTime={}".format(locatedAfterTime, locatedBeforeTime)

        @staticmethod
        def get_floor_image(campusName, buildingName, floorName):
            """This API returns an image for a given combination of Campus, Building and Floor name."""
            return "/config/v1/maps/image/{}/{}/{}".format(campusName, buildingName, floorName)

    