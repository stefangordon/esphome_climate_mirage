import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, climate_ir, remote_transmitter, remote_receiver, sensor
from esphome.const import CONF_ID, CONF_SENSOR

AUTO_LOAD = ["climate_ir"]

mirage_ns = cg.esphome_ns.namespace("mirage")
MirageClimate = mirage_ns.class_("MirageClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate.climate_schema(MirageClimate).extend(
    {
        cv.GenerateID(): cv.declare_id(MirageClimate),
        cv.Optional("transmitter_id"): cv.use_id(remote_transmitter.RemoteTransmitterComponent),
        cv.Optional("receiver_id"): cv.use_id(remote_receiver.RemoteReceiverComponent),
        cv.Optional(CONF_SENSOR): cv.use_id(sensor.Sensor),
        
        # These are the missing keys causing your KeyError
        cv.Optional("supports_cool", default=True): cv.boolean,
        cv.Optional("supports_heat", default=True): cv.boolean,
        cv.Optional("supports_dry", default=True): cv.boolean,
        cv.Optional("supports_fan_only", default=True): cv.boolean,
    }
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await climate_ir.register_climate_ir(var, config)
