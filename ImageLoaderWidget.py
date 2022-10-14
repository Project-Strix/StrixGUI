import sys
import inspect
from PySide6.QtWidgets import *
from Gui.ui_image_loader_form import Ui_imageLoaderForm
from monai_ex.transforms import LOADER, CHANNELER, ORIENTER, RESCALER, RESIZER, CROPADER, AUGMENTOR, UTILS
from enum import Enum

class OperatorRole(Enum):
   channelrole = 0
   cropaderrole = 1
   rescalerrole = 2 
   resizerrole = 3
   orientrole = 4
   augmentrole = 5
   utilrole = 6
   

class ImageLoaderWidget(QWidget):
   def __init__(self, parent = None) :
      super().__init__(parent)
      self.ui = Ui_imageLoaderForm()
      self.ui.setupUi(self) 
      self.ui.channelOperToolButton.clicked.connect(self.addChannelOperator)
      self.ui.orienTransToolButton.clicked.connect(self.addOrienTransOperator)
      self.ui.imageCropToolButton.clicked.connect(self.addimageCropOperator)
      self.ui.imageNormToolButton.clicked.connect(self.addImageNormOperator)
      self.ui.dataAugToolButton.clicked.connect(self.addDataAugOperator)
      self.ui.deleteToolButton.clicked.connect(self.deleteOperatorItem)
      self.ui.upToolButton.clicked.connect(self.upOperatorItem)
      self.ui.downToolButton.clicked.connect(self.downOperatorItem)
      self.initUi()
      self.initConfig()
      for x in self._loaders:
         self.ui.imageLoadFuncNameComboBox.addItem(x)
      if self._loaders:
         self.ui.imageLoadFuncNameComboBox.setCurrentIndex(0) 


   def initUi(self):
      radio_groupbox = QButtonGroup(self)
      radio_groupbox.addButton(self.ui.dim2dRadioButton)
      radio_groupbox.addButton(self.ui.dim25dRadioButton)
      radio_groupbox.addButton(self.ui.dim3dRadioButton)


   def updateData(self, ctrl, operator):
      pass 
   
   def updateUi(self, ctrl, operator):
      pass

         

   def initConfig(self):
      self._loaders = list(LOADER.keys())
      self._loader = self._loaders[0] if self._loaders else None
      self._channelers = list(CHANNELER.keys())
      self._channeler = self._channelers[0] if self._channelers else None
      self._cropaders = list(CROPADER.keys())
      self._cropader = self._cropaders[0] if self._cropaders else None
      # LOADER, CHANNELER, ORIENTER, RESCALER, RESIZER, CROPADER, AUGMENTOR, UTILS
      self._rescalers = list(RESCALER.keys())
      self._rescaler = self._rescalers[0] if self._rescalers else None
      self._resizers = list(RESIZER.keys())
      self._resizer = self._resizers[0] if self._resizers else None
      self._orienters = list(ORIENTER.keys())
      self._orienter = self._orienters[0] if self._orienters else None
      self._augmentors = list(AUGMENTOR.keys())
      self._augmentor = self._augmentors[0] if self._augmentors else None
      self._utils = list(UTILS.keys())
      self._util = self._utils[0] if self._utils else None
      self._operator_types = [self._loaders, self._channelers, self._cropaders, self._rescalers, self._resizers, 
      self._orienters, self._augmentors, self._utils]
      
   
   def getFuncArguments(self, func, prompt_all_args: bool = True):
      BUILTIN_TYPES = [dict, list, tuple, str, int, float, bool]
      sig = inspect.signature(func)
      anno = inspect.getfullargspec(func).annotations
      if not prompt_all_args:
            cond = lambda x: x[1].default is x[1].empty
      else:
            cond = lambda x: True

      # print("Prompt custom loss for", func, sig.parameters.items())
      for k, v in filter(cond, sig.parameters.items()):
            if anno.get(k) in BUILTIN_TYPES:
               default_value = None if v.default is v.empty else v.default
               print(anno[k], default_value)
            else:
               print(f"Cannot handle type '{anno.get(k)}' for argment '{k}'")

   def addChannelOperator(self):
      if self._channeler:
         index = self.ui.operItemsListWidget.count()
         item = QListWidgetItem(self._channeler)
         item.setWhatsThis("1")
         # item.setData(OperatorRole.channelrole.value, 1)
         # item.setText(self._channeler)
         # print("========", item.data(OperatorRole.channelrole.value)) #bug
         self.ui.operItemsListWidget.insertItem(index, item)

   def addOrienTransOperator(self):
      if self._orienter:
         index = self.ui.operItemsListWidget.count()
         item = QListWidgetItem(self._orienter)
         # item.setData(OperatorRole.orientrole, 5)
         item.setWhatsThis("5")
         self.ui.operItemsListWidget.insertItem(index, item)
   
   def addimageCropOperator(self):
      if self._cropader:
         index = self.ui.operItemsListWidget.count()
         item = QListWidgetItem(self)
         item.setText(self._cropader)
         # item.setData(OperatorRole.cropaderrole, 2)
         item.setWhatsThis("2")
         self.ui.operItemsListWidget.insertItem(index, self._cropader)

   def addImageNormOperator(self):
      if self._rescaler:
         index = self.ui.operItemsListWidget.count()
         item = QListWidgetItem(self._rescaler)
         # item.setData(OperatorRole.rescalerrole, 3)
         item.setWhatsThis("3")
         self.ui.operItemsListWidget.insertItem(index, item)

   def addDataAugOperator(self):
      if self._augmentor:
         index = self.ui.operItemsListWidget.count()
         item = QListWidgetItem(self._augmentor)
         # item.setData(OperatorRole.augmentrole, 6)
         item.setWhatsThis("6")
         self.ui.operItemsListWidget.insertItem(index, item)

   def downOperatorItem(self):
      current_index = self.ui.operItemsListWidget.currentIndex()
      current_item = self.ui.operItemsListWidget.currentItem()
      self.ui.operItemsListWidget.removeItemWidget(current_item)
      # new_items = []
      # for index in range(self.ui.operItemsListWidget.count()):
      #    new_items.append(QListWidgetItem("1"))
      #    # if index == current_index.row():
      #    #    continue
      #    # elif index == current_index.row() + 1:
      #    #    new_items.append(self.ui.operItemsListWidget.item(index).clone())
      #    #    new_items.append(self.ui.operItemsListWidget.item(current_index.row()).clone())
      #    # else:
      #    #    new_items.append(self.ui.operItemsListWidget.item(index).clone())
      # for index, item in enumerate(new_items):
      #    print(item.text())
      #    self.ui.operItemsListWidget.insertItem(index, item.text())
     
      # self.ui.operItemsListWidget.clear()
      # print(current_item, new_items[1])
      # for index, item in enumerate(new_items):
      #    self.ui.operItemsListWidget.insertItem(index, item.text())
         

     
      
      pass

   def upOperatorItem(self):
      pass

   def deleteOperatorItem(self):
      pass
      


