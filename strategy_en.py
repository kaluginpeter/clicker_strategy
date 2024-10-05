import heapq
import sys

"""
UNITS - a list of tuples, where each tuple represents a specific item.
Item characteristics:
   - Income Increase Per Hour. Indicates how much the income will rise after purchasing this item.
   - Cost. Indicates the amount of money required to purchase the item.
   - Name. Indicates the name of the item. Used for convenient output of calculation results.
By default, UNITS contains items available in the game "Clicker" from Yandex.
After purchasing an item, update the information about the item in UNITS.
"""
UNITS: list[tuple[float, float, str]] = [
    (1_960, 50_000, 'Бегущий по Плюсу'), (2_360, 50_000, 'Листинг'),
    (147, 42_820, 'Голубиное кабаре'), (210, 42_820, 'Маскарад'),
    (676, 104_940, 'Финансовая грамота'), (113, 64_580, 'Философский булыжник'),
    (393, 106_180, '24 на 7'), (338, 100_910, 'Козырное местечко'),
    (189, 59_950, 'Олимпийка'), (1_280, 531_700, 'Стильный черный пакет'),
    (316, 85_650, 'Голубильдер'), (315, 56_510, 'Цацка'),
    (421, 128_480, 'Кормящая рука'), (723, 199_800, 'Спа-набор'),
    (984, 235_960, 'Секретный сейф'), (232, 55_670, 'Пероплан'),
    (492, 70_780, 'Космобатут'), (984, 353_940, 'Журнал с анектодами'),
    (1_350, 322_910, 'Клюк да Винчи'), (1_890, 428_270, 'Покатушки'),
    (2_950, 589_900, 'Чистый памятник'), (3_930, 1_170_000, 'VR-Кандибобер'),
    (842, 235_540, 'В самый раз'), (1_890, 342_610, 'Зерновой прогноз'),
]


class StrategyCalculation:
    """
    Allows determining the best possible purchase of an item
    from a list of items. Uses a binary heap to calculate the results.
    The calculation involves two coefficients:
        - Return on Investment (ROI) coefficient.
        - Profitability coefficient.
    """
    def __init__(self) -> None:
        self.heap: list[tuple[float, float, str]] = []

    def adds_items(self, items: list[tuple[float, float, str]]) -> None:
        """
        Adds a list of items to the class storage.
        The input is expected to be a dataset similar to UNITS.
        """
        for item in items:
            value_per_hour, cost, name = item
            value_to_cost_ratio: float = value_per_hour / cost
            cost_to_value_ratio: float = cost / value_per_hour
            slot: tuple[float, float, str] = (
                -value_to_cost_ratio, cost_to_value_ratio, name
            )
            heapq.heappush(self.heap, slot)

    def whats_buy_next(self) -> str:
        """
        Outputs the best purchase that can be made from the given dataset.
        If there is no dataset, it raises an IndexError exception.
        The output is a string representing the name of the item.
        """
        if not self.heap:
            raise IndexError(
                "Nothing to buy! Please, add items in UNITS storage"
            )
        return self.heap[0][2]

    def best_5_items(self) -> list[str]:
        """
        Outputs the 5 best purchases that can be made from the given dataset.
        If there is no dataset, it raises an IndexError exception.
        If the dataset contains fewer than 5 items, the function will return all available items.
        The output is a list of strings, where each string represents the name of an item.
        The list is sorted in descending order, from the most profitable purchase to less profitable items.
        """
        output: list[str] = []
        for _ in range(min(5, len(self.heap))):
            output.append(heapq.heappop(self.heap)[2])
        return output


if __name__ == '__main__':
    strategy: StrategyCalculation = StrategyCalculation()
    strategy.adds_items(UNITS)
    sys.stdout.write('The bests item to buying - ')
    sys.stdout.write(strategy.whats_buy_next() + '\n')
    sys.stdout.write('-' * 15 + '\n')
    sys.stdout.write('The best 5 items to buy:\n')
    for choice in strategy.best_5_items():
        sys.stdout.write(choice + '\n')
