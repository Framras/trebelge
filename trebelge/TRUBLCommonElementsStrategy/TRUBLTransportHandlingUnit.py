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
        if totalgoodsitemquantity_ is not None:
            if totalgoodsitemquantity_.text is not None:
                frappedoc['totalgoodsitemquantity'] = totalgoodsitemquantity_.text
                frappedoc['totalgoodsitemquantityunitcode'] = totalgoodsitemquantity_.attrib.get('unitCode')
        # ['TotalPackageQuantity'] = ('cbc', '', 'Seçimli (0...1)', 'totalpackagequantityunitcode')
        totalpackagequantity_: Element = element.find('./' + cbcnamespace + 'TotalPackageQuantity')
        if totalpackagequantity_ is not None:
            if totalpackagequantity_.text is not None:
                frappedoc['totalpackagequantity'] = totalpackagequantity_.text
                frappedoc['totalpackagequantityunitcode'] = totalpackagequantity_.attrib.get('unitCode')
        # ['DamageRemarks'] = ('cbc', 'damageremarks', 'Seçimli (0...n)')
        damageremarks_: list = element.findall('./' + cbcnamespace + 'DamageRemarks')
        if len(damageremarks_) != 0:
            damageremarks: list = []
            for damageremark_ in damageremarks_:
                tmp = damageremark_.text
                if tmp is not None:
                    damageremarks.append(tmp)
            if len(damageremarks) != 0:
                frappedoc['damageremarks'] = damageremarks
        # ['MinimumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)')
        minimumtemperature_: Element = element.find('./' + cacnamespace + 'MinimumTemperature')
        if minimumtemperature_ is not None:
            tmp = TRUBLTemperature().process_element(minimumtemperature_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['minimumtemperature'] = tmp.name
        # ['MaximumTemperature'] = ('cac', 'Temperature', 'Seçimli (0...1)')
        maximumtemperature_: Element = element.find('./' + cacnamespace + 'MaximumTemperature')
        if maximumtemperature_ is not None:
            tmp = TRUBLTemperature().process_element(maximumtemperature_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['maximumtemperature'] = tmp.name
        # ['FloorSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)')
        floorspace_: Element = element.find('./' + cacnamespace + 'FloorSpaceMeasurementDimension')
        if floorspace_ is not None:
            tmp = TRUBLDimension().process_element(floorspace_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['floorspacemeasurementdimension'] = tmp.name
        # ['PalletSpaceMeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...1)')
        palletspace_: Element = element.find('./' + cacnamespace + 'PalletSpaceMeasurementDimension')
        if palletspace_ is not None:
            tmp = TRUBLDimension().process_element(palletspace_, cbcnamespace, cacnamespace)
            if tmp is not None:
                frappedoc['palletspacemeasurementdimension'] = tmp.name
        if frappedoc == {}:
            return None
        document: Document = self._get_frappedoc(self._frappeDoctype, frappedoc, False)
        # ['ActualPackage'] = ('cac', 'Package', 'Seçimli (0...n)', 'actualpackage')
        actualpackages_: list = element.findall('./' + cacnamespace + 'ActualPackage')
        if len(actualpackages_) != 0:
            actualpackage: list = []
            for actualpackage_ in actualpackages_:
                tmp = TRUBLPackage().process_element(actualpackage_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    actualpackage.append(tmp)
            if len(actualpackage) != 0:
                frappedoc['actualpackage'] = actualpackage
                document.actualpackage = actualpackage
                document.save()
        # ['TransportEquipment'] = ('cac', 'TransportEquipment', 'Seçimli (0...n)', 'transportequipment')
        transportequipment_: list = element.findall('./' + cacnamespace + 'TransportEquipment')
        if len(transportequipment_) != 0:
            transportequipment: list = []
            for equipment_ in transportequipment_:
                tmp = TRUBLTransportEquipment().process_element(equipment_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    transportequipment.append(tmp)
            if len(transportequipment) != 0:
                frappedoc['transportequipment'] = transportequipment
                document.transportequipment = transportequipment
                document.save()
        # ['TransportMeans'] = ('cac', 'TransportMeans', 'Seçimli (0...n)', 'transportmeans')
        transportmeans_: list = element.findall('./' + cacnamespace + 'TransportMeans')
        if len(transportmeans_) != 0:
            transportmeans: list = []
            for means_ in transportmeans_:
                tmp = TRUBLTransportMeans().process_element(means_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    transportmeans.append(tmp)
            if len(transportmeans) != 0:
                frappedoc['transportmeans'] = transportmeans
                document.transportmeans = transportmeans
                document.save()
        # ['HazardousGoodsTransit'] = ('cac', 'HazardousGoodsTransit', 'Seçimli (0...n)', 'hazardousgoodstransit')
        hazardousgoodstransit_: list = element.findall('./' + cacnamespace + 'HazardousGoodsTransit')
        if len(hazardousgoodstransit_) != 0:
            hazardousgoodstransit: list = []
            for goodstransit_ in hazardousgoodstransit_:
                tmp = TRUBLHazardousGoodsTransit().process_element(goodstransit_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    hazardousgoodstransit.append(tmp)
            if len(hazardousgoodstransit) != 0:
                frappedoc['hazardousgoodstransit'] = hazardousgoodstransit
                document.hazardousgoodstransit = hazardousgoodstransit
                document.save()
        # ['MeasurementDimension'] = ('cac', 'Dimension', 'Seçimli (0...n)', 'measurementdimension')
        measurementdimensions_: list = element.findall('./' + cacnamespace + 'MeasurementDimension')
        if len(measurementdimensions_) != 0:
            measurementdimension: list = []
            for measurementdimension_ in measurementdimensions_:
                tmp = TRUBLDimension().process_element(measurementdimension_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    measurementdimension.append(tmp)
            if len(measurementdimension) != 0:
                frappedoc['measurementdimension'] = measurementdimension
                document.measurementdimension = measurementdimension
                document.save()
        # ['ShipmentDocumentReference'] = ('cac', 'DocumentReference', 'Seçimli (0...n)', 'shipmentdocumentreference')
        shipmentdocumentreferences_: list = element.findall('./' + cacnamespace + 'ShipmentDocumentReference')
        if len(shipmentdocumentreferences_) != 0:
            shipmentdocumentreference: list = []
            for shipmentdocumentreference_ in shipmentdocumentreferences_:
                tmp = TRUBLDocumentReference().process_element(shipmentdocumentreference_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    shipmentdocumentreference.append(tmp)
            if len(shipmentdocumentreference) != 0:
                frappedoc['shipmentdocumentreference'] = shipmentdocumentreference
                document.shipmentdocumentreference = shipmentdocumentreference
                document.save()
        # ['CustomsDeclaration'] = ('cac', 'CustomsDeclaration', 'Seçimli (0...n)', 'customsdeclaration')
        customsdeclarations_: list = element.findall('./' + cacnamespace + 'CustomsDeclaration')
        if len(customsdeclarations_) != 0:
            customsdeclaration: list = []
            for customsdeclaration_ in customsdeclarations_:
                tmp = TRUBLCustomsDeclaration().process_element(customsdeclaration_, cbcnamespace, cacnamespace)
                if tmp is not None:
                    customsdeclaration.append(tmp)
            if len(customsdeclaration) != 0:
                frappedoc['customsdeclaration'] = customsdeclaration
                document.customsdeclaration = customsdeclaration
                document.save()

        return self._update_frappedoc(self._frappeDoctype, frappedoc, document)
