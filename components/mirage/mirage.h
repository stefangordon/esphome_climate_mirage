#pragma once

#include "esphome/components/climate_ir/climate_ir.h"
#include "esphome/components/remote_base/mirage_protocol.h"

namespace esphome {
namespace mirage {

class MirageClimate : public climate_ir::ClimateIR {
 public:
  MirageClimate()
      : climate_ir::ClimateIR(
            16.0, 30.0, 1.0, true, true,
            {climate::CLIMATE_FAN_AUTO, climate::CLIMATE_FAN_LOW, climate::CLIMATE_FAN_MEDIUM, climate::CLIMATE_FAN_HIGH},
            {climate::CLIMATE_SWING_OFF, climate::CLIMATE_SWING_VERTICAL, climate::CLIMATE_SWING_HORIZONTAL, climate::CLIMATE_SWING_BOTH}) {}

  // --- THIS IS THE FIX FOR YOUR COMPILATION ERROR ---
  // These allow the Python script to toggle modes on/off
  void set_supports_cool(bool supports_cool) { this->supports_cool_ = supports_cool; }
  void set_supports_heat(bool supports_heat) { this->supports_heat_ = supports_heat; }
  void set_supports_dry(bool supports_dry) { this->supports_dry_ = supports_dry; }
  void set_supports_fan_only(bool supports_fan_only) { this->supports_fan_only_ = supports_fan_only; }
  // -------------------------------------------------

 protected:
  void transmit_state() override;
  bool on_receive(remote_base::RemoteReceiveData data) override;
};

}  // namespace mirage
}  // namespace esphome
