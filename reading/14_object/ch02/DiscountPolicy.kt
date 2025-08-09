sealed class DiscountPolicyType {
    class Amount(val amount: Int) : DiscountPolicyType()
    class Ratio(val ratio: Float) : DiscountPolicyType()
}
class DiscountPolicy (val type: DiscountPolicyType) {
    fun discount(price: Int): Int {
        return when (val condition = this.type) {
            is DiscountPolicyType.Amount -> price - condition.amount
            is DiscountPolicyType.Ratio -> (price * (1 - condition.ratio)).toInt()
        }
    }
}
