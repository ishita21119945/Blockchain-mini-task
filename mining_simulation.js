import java.security.MessageDigest;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Block {
    public int index;
    public String timestamp;
    public String data;
    public String previousHash;
    public String hash;
    public int nonce;

    public Block(int index, String data, String previousHash) {
        this.index = index;
        this.timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        this.data = data;
        this.previousHash = previousHash;
        this.nonce = 0;
        this.hash = calculateHash();
    }
    public void mineBlock(int difficulty) {
    String target = new String(new char[difficulty]).replace('\0', '0'); // e.g., "0000"
    long startTime = System.currentTimeMillis();

    while (!hash.substring(0, difficulty).equals(target)) {
        nonce++;
        hash = calculateHash();
    }

    long endTime = System.currentTimeMillis();
    System.out.println("[✓] Block " + index + " mined!");
    System.out.println("     Hash:  " + hash);
    System.out.println("     Nonce: " + nonce);
    System.out.println("     Time Taken: " + (endTime - startTime) + " ms\n");
}


    public String calculateHash() {
        try {
            String input = index + timestamp + data + previousHash + nonce;
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hashBytes = digest.digest(input.getBytes("UTF-8"));
            StringBuilder hexString = new StringBuilder();

            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void printBlock() {
        System.out.println("Block " + index);
        System.out.println("  Hash: " + hash);
        System.out.println("  Prev: " + previousHash);
        System.out.println("  Data: " + data);
        System.out.println();
    }
}
