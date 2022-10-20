MainQuery = """
query($ts: DateTime, $noGasData: Boolean = false) {
    graphTs: getGraphs(ts: $ts) { ts }
    
    peopleOccupationIcons: getStorageRecord(id: "people-occupation-icons") { value }
    vehicleTypeIcons: getStorageRecord(id: "vehicle-type-icons") { value }

    devices: getDevices(ts: $ts, filter: { type: { include: [TAG, SENTRY, GATEWAY, RETRANSLATOR] } }) {
        ...Device
        location {
            ...Location
        }
        carrier {
            ...Carrier
        }
    }

    virtualDevices: getVirtualDevices(ts: $ts) {
        ...VDevice
        carrier_id
    }
}

fragment VDevice on VirtualDevice {
    id
    type
    attrs : attrs_raw
}  

fragment Device on Device {
    ts
    mac
    type
    cycle
    ver { hw sw }
    online
    accessibility
    uptime
    ip
    coord { edge { id } offset }
    area
    battery { voltage, voltage_int }

    attrs : attrs_raw

    GAS_CH4: sensor(type: GAS_CH4) @skip(if: $noGasData) {
        ... on Sensor_GAS_CH4 { value }
    } 
    GAS_CO: sensor(type: GAS_CO) @skip(if: $noGasData) {
        ... on Sensor_GAS_CO { value }
    } 
    GAS_CO2: sensor(type: GAS_CO2) @skip(if: $noGasData) {
        ... on Sensor_GAS_CO2 { value }
    } 
    GAS_O2: sensor(type: GAS_O2) @skip(if: $noGasData) {
        ... on Sensor_GAS_O2 { value }
    }
}

fragment Location on Location {
    ts
    coord {
        edge { id }
        offset
        areas {
            ...GraphArea
        }
    }
}

fragment GraphArea on GraphArea {
    id
    edges { id }
    attrs {
        name
        voiloc__autoarea_type
        sip__type
        sip__color
        opc__people_inside
    }
}

fragment Carrier on Carrier {
    id
    type
    ...on Carrier_PEOPLE {
        attrs : attrs_raw
        photo : attrs { photo }
    }
}
"""
