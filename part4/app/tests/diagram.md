       ┌───────────────────┐
       │   Repository      │  ← Abstract Base Class (ABC)
       │───────────────────│
       │ + add(obj)         │  ← abstractmethod
       │ + get(obj_id)      │  ← abstractmethod
       │ + get_all()        │  ← abstractmethod
       │ + update(id,data)  │  ← abstractmethod
       │ + delete(obj_id)   │  ← abstractmethod
       │ + get_by_attribute │  ← abstractmethod
       └───────────────────┘
                 ▲
                 │  (inherits from Repository)
                 │
       ┌────────────────────────┐
       │ InMemoryRepository     │  ← Concrete Class
       │────────────────────────│
       │ + add(obj)             │  ← implemented
       │ + get(obj_id)          │  ← implemented
       │ + get_all()            │  ← implemented
       │ + update(id,data)      │  ← implemented
       │ + delete(obj_id)       │  ← implemented
       │ + get_by_attribute     │  ← implemented
       └────────────────────────┘
                 │
                 │  (used by Facade or other code)
                 ▼
       ┌────────────────────────┐
       │ HBnBFacade             │
       │────────────────────────│
       │ user_repo = InMemoryRepository()
       │ place_repo = InMemoryRepository()
       │ ...                    │
       └────────────────────────┘


Route (Flask-RESTX)
    ↓  auth / permissions
Facade (HBnBFacade)
    ↓  orchestration only
Model (User)
    ↓  validation + business rules
Repository
    ↓  DB commit only