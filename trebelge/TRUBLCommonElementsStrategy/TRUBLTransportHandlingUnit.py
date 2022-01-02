from xml.etree.ElementTree import Element

from frappe.model.document import Document
from trebelge.TRUBLCommonElementsStrategy.TRUBLCommonElement import TRUBLCommonElement
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
            field_: Element = element.find('./' + cbcnamespace + elementtag_)
            if field_ is not None:
                if field_.text is not None:
                    frappedoc[elementtag_.lower()] = field_.text
        # ['TotalGoodsItemQuantity'] = ('cbc', '', 'Seçimli (0...1)', 'totalgoodsitemquantityunitcode')
        totalgoodsitemquantity_: Element = element.find('./' + cbcnamespace + 'TotalGoodsItemQuantity')
        if totalgoodsitemquantity_:
            frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
            frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalPackageQuantity'] = ('cbc', '', 'Seçimli (0...1)', 'totalpackagequantityunitcode')
        totalpackagequantity_: Element = element.find('./' + cbcnamespace + 'TotalPackageQuantity')
        if totalpackagequantity_:
            frappedoc['totalpackagequantity'] = totalpackagequantity_.text
            frappedoc['totalpackagequantityunitcode'] = totalpackagequantity_.attrib.get('unitCode')
        # ['DamageRemarks'] = ('cbc', 'damageremarks', 'Seçimli (0...n)')
        damageremarks_: list = element.findall('./' + cbcnamespace + 'DamageRemarks')
        if len(damageremarks_) != 0:
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
            tagelement_: Element = element.find('./' + cacnamespace + element_.get('Tag'))
            if tagelement_:
                frappedoc[element_.get('fieldName')] = element_.get('strategy').process_element(tagelement_,
                                                                                                cbcnamespace,
                                                                                                cacnamespace).name
        product = self._get_frappedoc(self._frappeDoctype, frappedoc)
        # ['ActualPackage'] = ('cac', 'Package', 'Seçimli (0...n)', 'actualpackage')
        actualpackages_: list = element.findall('./' + cacnamespace + 'ActualPackage')
        if len(actualpackages_) != 0:
            actualpackage: list = []
            for actualpackage_ in actualpackages_:
                actualpackage.append(TRUBLPackage().process_element(actualpackage_,
                                                                    cbcnamespace,
                                                                    cacnamespace))
            product.actualpackage = actualpackage
            product.save()
        # ['TransportEquipment'] = ('cac', 'TransportEquipment', 'Seçimli (0...n)', 'transportequipment')
        transportequipment_: list = element.findall('./' + cacnamespace + 'TransportEquipment')
        if len(transportequipment_) != 0:
            transportequipment: list = []
            for equipment_ in transportequipment_:
                transportequipment.append(TRUBLTransportEquipment().process_element(equipment_,
                                                                                    cbcnamespace,
                                                                                    cacnamespace))
            product.transportequipment = transportequipment
            product.save()
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...n)', 'transportmeans')
        transportmeans_: list = element.findall('./' + cacnamespace + 'TransportMeans')
        if len(transportmeans_) != 0:
            transportmeans: list = []
            for means_ in transportmeans_:
                transportmeans.append(TRUBLTransportMeans().process_element(means_,
                                                                            cbcnamespace,
                                                                            cacnamespace))
            product.transportmeans = transportmeans
            product.save()
        # ['HazardousGoodsTransit'] = ('cac', 'HazardousGoodsTransit', 'Seçimli (0...n)', 'hazardousgoodstransit')
        hazardousgoodstransit_: list = element.findall('./' + cacnamespace + 'HazardousGoodsTransit')
        if len(hazardousgoodstransit_) != 0:
            hazardousgoodstransit: list = []
            for goodstransit_ in hazardousgoodstransit_:
                hazardousgoodstransit.append(TRUBLHazardousGoodsTransit().process_element(goodstransit_,
                                                                                          cbcnamespace,
                                                                                          cacnamespace))
            product.hazardousgoodstransit = hazardousgoodstransit
            product.save()
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', 'measurementdimension')
        measurementdimensions_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if len(measurementdimensions_) != 0:
            measurementdimension: list = []
            for measurementdimension_ in measurementdimensions_:
                measurementdimension.append(TRUBLDimension().process_element(measurementdimension_,
                                                                             cbcnamespace,
                                                                             cacnamespace))
            product.measurementdimension = measurementdimension
            product.save()
        # ['ShipmentDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)', 'shipmentdocumentreference')
        shipmentdocumentreferences_: list = element.findall('./' + cacnamespace + 'ShipmentDocumentReference')
        if len(shipmentdocumentreferences_) != 0:
            shipmentdocumentreference: list = []
            for shipmentdocumentreference_ in shipmentdocumentreferences_:
                shipmentdocumentreference.append(TRUBLDocumentReference().process_element(shipmentdocumentreference_,
                                                                                          cbcnamespace,
                                                                                          cacnamespace))
            product.shipmentdocumentreference = shipmentdocumentreference
            product.save()
        # ['CustomsDeclaration'] = ('cac', 'CustomsDeclaration', 'Seçimli (0...n)', 'customsdeclaration')
        customsdeclarations_: list = element.findall('./' + cacnamespace + 'CustomsDeclaration')
        if len(customsdeclarations_) != 0:
            customsdeclaration: list = []
            for customsdeclaration_ in customsdeclarations_:
                customsdeclaration.append(TRUBLCustomsDeclaration().process_element(customsdeclaration_,
                                                                                    cbcnamespace,
                                                                                    cacnamespace))
            product.customsdeclaration = customsdeclaration
            product.save()

        return product
