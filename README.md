# NexusDL
NexusDL is an automatic NexusMods modlist downloader - that's it! It allows for bulk-downloads of Wabbajack modlists for games like Skyrim, while completely bypassing the "click to download" prompt when using the NexusMods free tier.
<br>

## Config File

The config file for this application includes various configuration to modify aspects of the program such as download location and threads amount. Below are the available options:

- **`cache_file`**: `"./downloadedmods.json"`: Path to the cache file that stores information about downloaded mods, including their download links and download status.
- **`download_dir`**: `"./download"`: The directory where downloaded mods will be stored.
- **`temp_dir`**: `"./temp"`: Directory where mods will be downloaded initially before being moved to the download directory.
- **`modlist_file`**: `"./modlist"`: The path to the Wabbajack modlist used for downloading mods.
- **`threads`**: `6`: The number of simultaneous downloads allowed. A higher value may cause rate limits from NexusMods. (6 or lower is recommended)
- **`nexus_sessions`**: `[]`: A list of your nexus mods session tokens, more than one would allow for multi sessions. If `multi_sessions` is enabled, the amount of tokens should match the thread amount.
- **`multi_sessions`**: `false`: *(Work in Progress: Leave this as `false` for now)* Enables each thread to use its own NexusMods session token for faster download speeds.

<br>

## Obtaining your NexusMods session token
Your Nexus session token is used to authenticate into NexusMods and is required for downloading any mod on their platform. After running the program for the first time, the config file will be generated with a placeholder value for the token. Replace it with your actual token after following the steps below.

1. Login to your NexusMods account on **nexusmods.com**
2. Open your browser's developer console with `CTRL + SHIFT + I`, or by right-clicking anywhere and clicking Inspect Element
3. Navigate to the **Storage**/**Application** tab and select **Cookies** (the name of the tab depends on your browser)
4. Copy the value for the `nexusmods_session` cookie by double clicking on the **Value** field and pressing `CTRL + C`

<br>

## Extracting the modlist file from Wabbajack
NexusDL also requires a Wabbajack `modlist` file which is used for downloading mods. This file could be extracted by following the steps below

1. Navigate to the directory where Wabbajack is installed. Inside, you will find a directory that is named after the version of Wabbajack installed. (ex: 3.7.5.1)
2. Enter the `downloaded_mod_lists` directory and locate the file for your downloaded modlist. Ensure it is a **.wabbajack** file (not a .metadata file.)
3. Extract the file using any archive tool such as 7-Zip or Winrar, and locate the `modlist` file inside. (this file has no file extension)
4. Copy this file to the directory where NexusDL is installed.