from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElementContext import TRUBLCommonElementContext
from trebelge.TRUBLCommonElementsStrategy.TRUBLCustomsDeclaration import TRUBLCustomsDeclaration
from trebelge.TRUBLCommonElementsStrategy.TRUBLDimension import TRUBLDimension
from trebelge.TRUBLCommonElementsStrategy.TRUBLDocumentReference import TRUBLDocumentReference
from trebelge.TRUBLCommonElementsStrategy.TRUBLHazardousGoodsTransit import TRUBLHazardousGoodsTransit
from trebelge.TRUBLCommonElementsStrategy.TRUBLPackage import TRUBLPackage
from trebelge.TRUBLCommonElementsStrategy.TRUBLTemperature import TRUBLTemperature
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportEquipment import TRUBLTransportEquipment
from trebelge.TRUBLCommonElementsStrategy.TRUBLTransportMeans import TRUBLTransportMeans


class TRUBLTransportHandlingUnit(TRUBLCommonElement):
    _frappeDoctype = 'UBL TR TransportHandlingUnit'
    _strategyContext: TRUBLCommonElementContext = TRUBLCommonElementContext()

    def process_element(self, element: Element, cbcnamespace: str, cacnamespace: str) -> Document:
        frappedoc: dict = {}
        # ['ID'] = ('cbc', 'id', 'Seçimli (0...1)')
        # ['TransportHandlingUnitTypeCode'] = ('cbc', 'transporthandlingunittypecode', 'Seçimli (0...1)')
        # ['HandlingCode'] = ('cbc', 'handlingcode', 'Seçimli (0...1)')
        # ['HandlingInstructions'] = ('cbc', 'handling-instructions', 'Seçimli (0...1)')
        # ['HazardousRiskIndicator'] = ('cbc', 'hazardousriskindicator', 'Seçimli (0...1)')
        # ['TraceID'] = ('cbc', 'traceid', 'Seçimli (0...1)')
        cbcsecimli01: list = ['ID', 'TransportHandlingUnitTypeCode', 'HandlingCode', 'HandlingInstructions',
                              'HazardousRiskIndicator', 'TraceID']
        for elementtag_ in cbcsecimli01:
            field_: Element = element.find(cbcnamespace + elementtag_)
            if not field_ is not None:
                frappedoc[field_.tag.lower()] = field_.text
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)', 'totalgoodsitemquantityunitcode')
        totalgoodsitemquantity_: Element = element.find(cbcnamespace + 'TotalGoodsItemQuantity')
        if not totalgoodsitemquantity_ is not None:
            frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
            frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalPackageQuantity'] = ('cbc', '', 'Seçimli (0...1)', 'totalpackagequantityunitcode')
        totalpackagequantity_: Element = element.find(cbcnamespace + 'TotalPackageQuantity')
        if not totalpackagequantity_ is not None:
            frappedoc['totalpackagequantity'] = totalpackagequantity_.text
            frappedoc['totalpackagequantityunitcode'] = totalpackagequantity_.attrib.get('unitCode')
        # ['DamageRemarks'] = ('cbc', 'damageremarks', 'Seçimli (0...n)')
        damageremarks_: list = element.findall(cbcnamespace + 'DamageRemarks')
        if not damageremarks_ is not None:
            damageremarks: list = []
            for damageremark_ in damageremarks_:
                damageremarks.append(damageremark_.text)
            frappedoc['damageremarks'] = damageremarks
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)')
        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)')
        # ['FloorSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)')
        # ['PalletSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)')
        cacsecimli01: list = \
            [{'Tag': 'MinimumTemperature', 'strategy': TRUBLTemperature(), 'fieldName': 'minimumtemperature'},
             {'Tag': 'MaximumTemperature', 'strategy': TRUBLTemperature(), 'fieldName': 'maximumtemperature'},
             {'Tag': 'FloorSpaceMeasurementDimension', 'strategy': TRUBLDimension(),
              'fieldName': 'floorspacemeasurementdimension'},
             {'Tag': 'PalletSpaceMeasurementDimension', 'strategy': TRUBLDimension(),
              'fieldName': 'palletspacemeasurementdimension'}
             ]
        for element_ in cacsecimli01:
            tagelement_: Element = element.find(cacnamespace + element_.get('Tag'))
            if not tagelement_ is not None:
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                frappedoc[element_.get('fieldName')] = [self._strategyContext.return_element_data(tagelement_,
                                                                                                  cbcnamespace,
                                                                                                  cacnamespace)]
        # ['ActualPackage'] = ('cac', 'Package', 'Seçimli (0...n)')
        # ['TransportEquipment'] = ('cac', 'TransportEquipment', 'Seçimli (0...n)')
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...n)')
        # ['HazardousGoodsTransit'] = ('cac', 'HazardousGoodsTransit', 'Seçimli (0...n)')
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)')
        # ['ShipmentDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)')
        # ['CustomsDeclaration'] = ('cac', 'CustomsDeclaration', 'Seçimli (0...n)')
        cacsecimli01: list = \
            [{'Tag': 'ActualPackage', 'strategy': TRUBLPackage(), 'fieldName': 'actualpackage'},
             {'Tag': 'TransportEquipment', 'strategy': TRUBLTransportEquipment(), 'fieldName': 'transportequipment'},
             {'Tag': 'TransportMeans', 'strategy': TRUBLTransportMeans(), 'fieldName': 'transportmeans'},
             {'Tag': 'HazardousGoodsTransit', 'strategy': TRUBLHazardousGoodsTransit(),
              'fieldName': 'hazardousgoodstransit'},
             {'Tag': 'MeasurementDimension', 'strategy': TRUBLDimension(), 'fieldName': 'measurementdimension'},
             {'Tag': 'ShipmentDocumentReference', 'strategy': TRUBLDocumentReference(),
              'fieldName': 'shipmentdocumentreference'},
             {'Tag': 'CustomsDeclaration', 'strategy': TRUBLCustomsDeclaration(), 'fieldName': 'customsdeclaration'}
             ]
        for element_ in cacsecimli01:
            tagelements_: list = element.findall(cacnamespace + element_.get('Tag'))
            if not tagelements_ is not None:
                tagelements: list = []
                strategy: TRUBLCommonElement = element_.get('strategy')
                self._strategyContext.set_strategy(strategy)
                for tagelement in tagelements_:
                    tagelements.append(self._strategyContext.return_element_data(tagelement,
                                                                                 cbcnamespace,
                                                                                 cacnamespace))
                frappedoc[element_.get('fieldName')] = tagelements

        return self._get_frappedoc(self._frappeDoctype, frappedoc)
