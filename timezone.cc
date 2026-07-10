#include <chrono>

extern "C" void c_to_local(char* timezone_str, long long* timestamp) {
    const std::chrono::time_zone* tz = std::chrono::locate_zone(timezone_str);
    std::chrono::sys_time<std::chrono::seconds> tp{std::chrono::seconds(*timestamp)};
    auto local_tp = tz->to_local(tp);
    *timestamp = local_tp.time_since_epoch().count();
}
