import java.util.ArrayList;

public class BlockchainTest {
    public static void main(String[] args) {
        ArrayList<Block> blockchain = new ArrayList<>();

        Block genesis = new Block(0, "Genesis Block", "0");
        blockchain.add(genesis);

        Block block1 = new Block(1, "Block 1 Data", genesis.hash);
        blockchain.add(block1);

        Block block2 = new Block(2, "Block 2 Data", block1.hash);
        blockchain.add(block2);

        System.out.println("🧱 Blockchain:");
        for (Block block : blockchain) {
            block.printBlock();
        }

        System.out.println("[!] Tampering Block 1...\n");
        block1.data = "Tampered Block 1 Data";
        block1.hash = block1.calculateHash();

        System.out.println("[*] Validating blockchain...\n");
        for (int i = 1; i < blockchain.size(); i++) {
            Block current = blockchain.get(i);
            Block previous = blockchain.get(i - 1);

            if (!current.previousHash.equals(previous.hash)) {
                System.out.println("[X] Block " + i + " is INVALID!");
            } else {
                System.out.println("[OK] Block " + i + " is valid.");
            }
        }
    }
}
