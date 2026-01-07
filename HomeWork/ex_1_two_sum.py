# Дан список чисел nums и целое чилсо target. Вернуть индекс двух чисел сумма которых равна target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Создаётся метод, который получает список nums и число target
        # Должны получить от этого метода тоже список
        slovar = {} # Создаём словарь
        for i, n in enumerate(nums): # Используем цикл от i(индекс) и n(значения) в списке nums
            # функция enumerate возвращает i(индекс) и n(значения) списка
            num = target - n
            if num in slovar:
                return [slovar[num],i]
            slovar[n] = i
        return