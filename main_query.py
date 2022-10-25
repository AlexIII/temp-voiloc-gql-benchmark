MainQuery = """
query($ts: DateTime) {
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

    getSensors(ts: $ts, filter: {type: {include: [GAS_O2, GAS_CO, GAS_CH4, GAS_CO2]}}) {
        ts
        mac
        type
        ...on Sensor_GAS_CH4 { value }
        ...on Sensor_GAS_CO { value }
        ...on Sensor_GAS_CO2 { value }
        ...on Sensor_GAS_O2 { value }
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
