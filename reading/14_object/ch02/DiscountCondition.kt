import java.time.DayOfWeek
import java.time.LocalDate
import java.time.LocalTime

// Sealed class for discount condition types
sealed class DiscountConditionType {
    class Order(val order: Int) : DiscountConditionType()
    class Period(val dayOfWeek: DayOfWeek, val startTime: LocalTime, val endTime: LocalTime) : DiscountConditionType()
}

// Screening class using LocalDate and LocalTime
class Screening(val date: LocalDate, val startTime: LocalTime, val order: Int)

// DiscountCondition class with the isApply method
class DiscountCondition(val type: DiscountConditionType) {
    fun isApply(screening: Screening): Boolean {
        return when (val condition = this.type) {
            is DiscountConditionType.Order -> screening.order == condition.order
            is DiscountConditionType.Period -> {
                screening.date.dayOfWeek == condition.dayOfWeek &&
                screening.startTime in condition.startTime..condition.endTime
            }
        }
    }
}
