Tests Unitarios del Backend
=============================
Prueban la lógica de negocio de los Services de forma aislada.
Los Repositories se mockean con unittest.mock o pytest-mock.
Cada test es rápido (<10ms) y no necesita base de datos ni red.
Convención de nombres: test_[modulo]_[escenario]_[resultado_esperado].py
