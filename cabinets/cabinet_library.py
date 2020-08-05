from ..pc_lib import pc_types, pc_unit, pc_utils
from . import data_cabinets
from . import data_cabinet_doors
from . import data_cabinet_carcass
from . import data_appliances
from . import data_cabinet_splitter

class Base_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Base_Advanced()
        self.interior = None
        self.exterior = data_cabinet_doors.Door()
        self.splitter = None
        

class Tall_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Tall_Advanced()
        self.interior = None
        self.exterior = data_cabinet_doors.Door()
        self.splitter = None


class Upper_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Upper_Advanced()
        self.interior = None
        self.exterior = data_cabinet_doors.Door()
        self.splitter = None


class Drawer_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Base_Advanced()
        self.interior = None
        self.exterior = data_cabinet_doors.Drawers()
        self.exterior.drawer_qty = 3
        self.splitter = None


class Open_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Base_Advanced()
        self.interior = None
        self.exterior = None
        self.splitter = None        


class Splitter_Cabinet(data_cabinets.Standard_Cabinet):

    def __init__(self):
        self.carcass = data_cabinet_carcass.Tall_Advanced()
        self.interior = None
        self.exterior = None
        self.splitter = data_cabinet_splitter.Vertical_Splitter()
        self.splitter.vertical_openings = 4    

class Range(data_appliances.Range):

    def __init__(self):
        self.obj = None 