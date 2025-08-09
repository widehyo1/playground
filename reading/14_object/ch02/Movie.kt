class Movie(
    val title: String,
    val duration: Int, // in minutes
    val price: Int, // base price in cents or currency unit
    var discountPolicy: DiscountPolicy? = null,
) {
    private val screeningList: MutableList<Screening> = mutableListOf()
    private val discountConditionList: MutableList<DiscountCondition> = mutableListOf()

    fun addScreening(screening: Screening) {
        screeningList.add(screening)
    }

    fun getScreenings(): List<Screening> = screeningList.toList()

    fun addDiscountCondition(discountCondition: DiscountCondition) {
        discountConditionList.add(discountCondition)
    }

    fun getDiscountConditions(): List<DiscountCondition> = discountConditionList.toList()
}
