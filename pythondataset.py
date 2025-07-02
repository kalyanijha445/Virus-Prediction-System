import pandas as pd

virus_names = [
    # 75 malicious names (make sure there are exactly 75)
    'TrojanHorse', 'SpywareAgent', 'AdwareX', 'KeyLoggerPro', 'WormWin32',
    'MalwareBytes', 'RansomWareLock', 'RootkitDetector', 'CryptoLocker',
    'BackdoorAgent', 'PhishingTool', 'BotnetMaster', 'ExploitKit',
    'FakeAV', 'SpyBot', 'AdClicker', 'DownloaderX', 'HijackerPro',
    'TrojanSpy', 'MaliciousPDF', 'KeyloggerLite', 'ZeroDayExploit',
    'RemoteAccessTool', 'PasswordStealer', 'DataExfiltrator', 'SessionHijack',
    'BankingTrojan', 'DriveByDownload', 'DNSChanger', 'ExploitPayload',
    'SpywareZilla', 'BackdoorX', 'RootkitZ', 'Cryptojacker', 'FakeInstaller',
    'ExploitInjector', 'MalwareDropper', 'VirusGenerator', 'RogueSecurity',
    'BotnetAgent', 'NetworkSniffer', 'PacketInterceptor', 'CredentialStealer',
    'VirusLoader', 'KeyloggerElite', 'SpamBot', 'AdFraud', 'ExploitScanner',
    'WormX', 'TrojanDropper', 'SilentSpy', 'MaliciousMacro', 'BotnetZombie',
    'TrojanDownloader', 'FakeUpdate', 'MalwareInjector', 'CredentialHarvester',
    'RansomCrypt', 'RemoteSpy', 'WebExploit', 'MaliciousScript', 'RootkitMaster',
    'SpywareHunter', 'VirusMorph', 'StealthBackdoor', 'AdwareKing', 'DropperX',
    'HijackTool', 'ExploitWorm', 'FakeTool', 'MalwareSpy', 'TrojanHorseX',
    'KeyloggerProPlus', 'WormXtreme', 'CryptoVirus', 'BackdoorElite',
    'SpamGenerator', 'PhishingKit', 'VirusRemoverFake', 'RootkitPro',
    'TrojanBlaster', 'MaliciousDownloader', 'AdwarePro', 'SpywareElite',
    'RansomWarePro', 'DataTheftAgent', 'ExploitBot', 'VirusScannerFake',
    'KeyloggerUltimate', 'WormAgent', 'FakeCleaner', 'MalwareBot', 'TrojanHunter',
    'BackdoorSpy', 'RootkitAgent'
]

normal_apps = [
    # 50 clean software names (make sure exactly 50)
    'VirusCleaner', 'SystemUtility', 'AntivirusGuard', 'SafeApp',
    'WindowsUpdater', 'CleanManager', 'PatchUpdater', 'RegistryFixer',
    'NormalApp', 'FileExplorer', 'DiskManager', 'BackupTool', 'TaskScheduler',
    'SystemMonitor', 'ResourceManager', 'DriverUpdater', 'SecurityScanner',
    'UpdateAgent', 'FileCompressor', 'NetworkManager', 'BatterySaver',
    'PerformanceBooster', 'SystemOptimizer', 'StartupManager', 'ProcessExplorer',
    'MemoryCleaner', 'DiskDefragmenter', 'FirewallManager', 'SoftwareInstaller',
    'UninstallerPro', 'SystemTweaker', 'PowerManager', 'LogCleaner',
    'CacheCleaner', 'ClipboardManager', 'ScreenRecorder', 'PasswordManager',
    'NoteKeeper', 'EmailClient', 'CalendarApp', 'PhotoViewer', 'VideoPlayer',
    'MusicPlayer', 'PDFReader', 'TextEditor', 'WebBrowser', 'CloudSync',
    'BackupPro', 'FileEncryptor', 'SystemReporter', 'UpdateManager', 'DiskScanner'
]

data = {
    'VirusName': virus_names + normal_apps,
    'Label': [1]*len(virus_names) + [0]*len(normal_apps)
}

print(len(data['VirusName']))  # should print 125
print(len(data['Label']))      # should print 125

df = pd.DataFrame(data)
df.to_csv('virus_dataset_large.csv', index=False)
print("✅ Large virus_dataset_large.csv created successfully.")
