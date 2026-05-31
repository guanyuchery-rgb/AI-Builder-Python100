# Day08 - 面向对象基础与 dataclass

学习定位：通过真实领域模型理解类和对象，并使用 `dataclass` 减少样板代码。

## 今日目标

- 理解类、对象、属性、方法。
- 知道什么时候 OOP 有用，什么时候没必要。
- 使用 `dataclass` 表达简单数据模型。
- 建模金融或 Agent 场景里的小实体。


## 知识点 1：类与对象

### 定义

类定义一种对象的结构和行为。对象是类创建出来的具体实例。

### 为什么存在

当一组数据和行为天然属于同一个概念时，类能让代码更清楚。

### 最小案例

```python
class Position:
    def __init__(self, symbol: str, shares: int, price: float) -> None:
        self.symbol = symbol
        self.shares = shares
        self.price = price

    def market_value(self) -> float:
        return self.shares * self.price


position = Position("AAPL", 10, 102.5)
print(position.market_value())
```

### 常见错误

- 忘记 `self`。
- 把无关行为塞进一个类。
- 修改对象状态却没有规则。

### 工程应用

- 领域模型。
- API 请求和响应对象。
- 策略配置。
- Agent 任务对象。

### 未来扩展

- `dataclass`。
- property。
- 继承与组合。
- Pydantic model。

## 知识点 2：dataclass

### 定义

`dataclass` 会自动生成常见方法，适合主要用于保存数据的小类。

### 为什么存在

它减少重复样板代码，让简单领域模型更清楚。

### 最小案例

```python
from dataclasses import dataclass


@dataclass
class Position:
    symbol: str
    shares: int
    price: float

    def market_value(self) -> float:
        return self.shares * self.price


position = Position("MSFT", 5, 210.0)
print(position)
print(position.market_value())
```

### 常见错误

- 明明 dict 足够，却强行写类。
- 可变默认值使用错误。
- 一个模型承担太多职责。

### 工程应用

- 清洗后的数据记录。
- 配置对象。
- 回测持仓。
- Agent 任务定义。

### 未来扩展

- `field(default_factory=list)`。
- frozen dataclass。
- Pydantic 数据验证。

## 现代代码示例：Agent 任务模型

```python
from dataclasses import dataclass


@dataclass
class AgentTask:
    name: str
    instruction: str
    verified: bool = False

    def mark_verified(self) -> None:
        self.verified = True


task = AgentTask("clean_prices", "规范化价格 CSV 行")
task.mark_verified()
print(task)
```

## AI 时代补充

```text
我有一段基于字典的 Python 代码。
请判断它应该继续用 dict，还是改成 dataclass。
用初学者能理解的方式说明取舍。
```


## Debug 日志

- `TypeError`：创建对象时缺参数。
- 值不对：检查对象属性。
- 设计问题：类名模糊，或做了太多事。

## 面试角度

OOP 适合把相关数据和行为放在一起，但不代表所有代码都应该写成类。

## Quant 关联

持仓、交易、订单、信号、组合快照都可以建模成小类。

## Agent 关联

Agent 任务、工具调用、验证结果可以显式建模，减少到处传松散 dict。

## 复习检查

- [ ] 我能定义简单类。
- [ ] 我能解释 `self`。
- [ ] 我能使用 `dataclass`。
- [ ] 我能判断 class 和 dict 的取舍。

## 简单路线 7 题（不超前）

只用今天及之前学过的能力。做不出来时，先回看当天最小案例，不跳到后面知识。

1. 用 class 或 dataclass 表示一条记录。
2. 给对象写一个返回金额的小方法。
3. 创建 2 个对象并打印字段。
4. 把 dict 改成数据对象。
5. 写一个列表保存多个对象。
6. 写一个汇总对象列表的函数。
7. 记录一次字段名写错的问题。
## 题目驱动训练

### 参考题 / 资料

- [LeetCode 1603 - Design Parking System](https://leetcode.com/problems/design-parking-system/)
- [LeetCode 705 - Design HashSet](https://leetcode.com/problems/design-hashset/)
- [Python dataclasses docs](https://docs.python.org/3/library/dataclasses.html)

### 5 道递进题

#### 1. Easy - Parking System

关联题：[LeetCode 1603](https://leetcode.com/problems/design-parking-system/)

题目：设计停车系统，车辆进入时扣减容量。

讲解：类适合管理“有状态”的对象。

```python
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # 用 dict 保存不同类型剩余车位
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.slots.get(carType, 0) <= 0:
            return False
        self.slots[carType] -= 1
        return True
```

#### 2. Easy - 简化 HashSet

关联题：[LeetCode 705](https://leetcode.com/problems/design-hashset/)

题目：实现 add/remove/contains。

讲解：先用 Python 内置 set 理解接口设计。

```python
class MyHashSet:
    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        self.data.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.data
```

#### 3. Medium - Trade dataclass

题目：用 dataclass 表示一笔交易。

讲解：数据对象要清楚字段，不要让 dict 到处乱飞。

```python
from dataclasses import dataclass

@dataclass
class Trade:
    symbol: str
    side: str
    quantity: int
    price: float

    def notional(self) -> float:
        return self.quantity * self.price
```

#### 4. Medium - Portfolio 汇总

题目：Portfolio 能添加交易，并计算总成交金额。

讲解：对象组合比全局变量更适合长期维护。

```python
class Portfolio:
    def __init__(self):
        self.trades: list[Trade] = []

    def add_trade(self, trade: Trade) -> None:
        self.trades.append(trade)

    def total_notional(self) -> float:
        return sum(trade.notional() for trade in self.trades)
```

#### 5. Hard - Agent ToolSpec

题目：定义工具名、描述、必填参数，并校验输入。

讲解：Agent tool 的稳定性从清楚 schema 开始。

```python
from dataclasses import dataclass

@dataclass
class ToolSpec:
    name: str
    description: str
    required_fields: list[str]

    def validate(self, payload: dict) -> list[str]:
        # 返回缺失字段，而不是直接抛异常
        return [field for field in self.required_fields if field not in payload]
```
