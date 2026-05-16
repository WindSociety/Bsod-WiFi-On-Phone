import ctypes
from ctypes import wintypes

# Загружаем ntdll.dll
ntdll = ctypes.windll.ntdll

# Даем процессу необходимые привилегии
# 19 = SE_SHUTDOWN_PRIVILEGE
# Необходимо для вызова NtRaiseHardError
try:
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(ctypes.c_bool()))
except Exception as e:
    print(f"Ошибка при получении привилегии: {e}")
    sys.exit(1)

# Вызываем синий экран
# Статус 0xC0000022 (STATUS_ACCESS_VIOLATION) или 0xC000021A (STATUS_SYSTEM_PROCESS_TERMINATED)
# Параметр 6 заставляет систему выполнить перезагрузку после падения
try:
    ntdll.NtRaiseHardError(0xC000021A, 0, 0, None, 6, ctypes.byref(ctypes.c_ulong()))
except Exception as e:
    print(f"Ошибка при вызове NtRaiseHardError: {e}")
    sys.exit(1)